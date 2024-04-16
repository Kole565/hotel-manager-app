from bin.db import DB
from bin.gui.search_widget import SearchWidget
from bin.gui.entry_edit_widget import EntryEditWidget
from bin.gui.page_counter_widget import PageCounterWidget
from bin.gui.adding_dialog import AddingDialog
from bin.gui.rent_controller import RentController

from PySide6.QtCore import QSize
from PySide6.QtWidgets import (QMainWindow, QWidget, QMessageBox,
    QVBoxLayout, QHBoxLayout, QTableWidget, QGridLayout,
    QTableWidgetItem, QDialog, QDialogButtonBox, QToolBar)

from PySide6.QtGui import QAction



class TablesWindow(QMainWindow):

    DB_NAME = "test_db"
    USER = "test"

    TABLE_INITIALIZING_SALES_APPLYING = "rents"
    TABLE_WITH_TRANSACTIONS = "transactions"

    def __init__(self):
        super().__init__()

        self.setFixedSize(QSize(800, 450))

        self.db = DB(self.DB_NAME, self.USER)

        self.search_panel = SearchWidget(self.fetch)
        self.table_widget = QTableWidget()
        self.entry_edit_widget = EntryEditWidget(self.add, self.remove, self.edit)
        self.page_counter = PageCounterWidget()

        toolbar = QToolBar("Tables Toolbar")
        self.addToolBar(toolbar)

        names = ["rooms", "clients", "rents", "transactions", "clients_rents", "sales"]

        self.tables_switching_actions = [
            QAction("Rooms"),
            QAction("Clients"),
            QAction("Rents"),
            QAction("Transactions"),
            QAction("Clients/Rents"),
            QAction("Sales"),
        ]
        self.tables_switching_actions[0].triggered.connect(lambda: self.fetch(names[0]))
        toolbar.addAction(self.tables_switching_actions[0])
        self.tables_switching_actions[1].triggered.connect(lambda: self.fetch(names[1]))
        toolbar.addAction(self.tables_switching_actions[1])
        self.tables_switching_actions[2].triggered.connect(lambda: self.fetch(names[2]))
        toolbar.addAction(self.tables_switching_actions[2])
        self.tables_switching_actions[3].triggered.connect(lambda: self.fetch(names[3]))
        toolbar.addAction(self.tables_switching_actions[3])
        self.tables_switching_actions[4].triggered.connect(lambda: self.fetch(names[4]))
        toolbar.addAction(self.tables_switching_actions[4])
        self.tables_switching_actions[5].triggered.connect(lambda: self.fetch(names[5]))
        toolbar.addAction(self.tables_switching_actions[5])

        layout = QVBoxLayout()
        layout_for_table = QHBoxLayout()

        layout.addWidget(self.search_panel)
        layout_for_table.addWidget(self.table_widget)
        layout_for_table.addWidget(self.entry_edit_widget)
        layout.addLayout(layout_for_table)
        layout.addWidget(self.page_counter)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def fetch(self, table_name):
        self.db.connect()
        self.headers = self._get_headers(table_name)
        data = self._get_data(table_name)
        self.db.disconnect()

        self._show_data(data)

        self.active_table = table_name

    def refresh(self):
        self.fetch(self.active_table)

    def _get_data(self, table_name):
        self.db.execute("SELECT * FROM {}".format(table_name))
        data = self.db.fetch()

        return data

    def _get_headers(self, table_name):
        self.db.execute("SELECT column_name FROM information_schema.columns WHERE table_name = '{}'".format(table_name))
        headers = self.db.fetch()

        return headers

    def _show_data(self, data):
        self.table_widget.setRowCount(len(data))
        if data:
            self.table_widget.setColumnCount(len(data[0]))
        else:
            self.table_widget.setColumnCount(0)

        for x in range(len(data)):
            for y in range(len(data[0])):
                new_item = QTableWidgetItem(str(data[x][y]))
                self.table_widget.setItem(x, y, new_item)

        self.table_widget.sortItems(0)

    def add(self):
        self.db.connect()

        collected_data = []
        if self.headers[0][0] == "id":
            size = len(self.headers) - 1, 1
            if self.active_table == "rents":
                dialog = RentController(self.db)
            else:
                dialog = AddingDialog(size, self.headers[1:], collected_data)
        else:
            size = len(self.headers), 1
            dialog = AddingDialog(size, self.headers[:], collected_data)

        if not dialog.exec():
            return

        if self.active_table == self.TABLE_INITIALIZING_SALES_APPLYING:
            room_cost_query = "SELECT price FROM rooms WHERE id = %s;"

            self.db.execute(room_cost_query, collected_data[0])
            room_cost = self.db.fetch()

            transaction_id = collected_data[1]
            transaction_value = room_cost[0]

            self._get_or_create_transaction(transaction_id, transaction_value)
            self.apply_sales(transaction_id)

        self._add_item(self.active_table, collected_data, self.headers[1:])
        self.refresh()

        self.db.disconnect()

    def _get_or_create_transaction(self, transaction_id, transaction_value):
        is_transaction_exist_query = "SELECT 1 FROM {} WHERE id = %s;".format(self.TABLE_WITH_TRANSACTIONS)
        self.db.execute(is_transaction_exist_query, transaction_id)
        result = self.db.fetch()

        print("Result from checking is transaction exist: {}".format(result))

        if result:
            return result

        self._create_transaction(transaction_id, transaction_value)

    def _create_transaction(self, transaction_id, transaction_value):
        create_query = "INSERT INTO {} (id, sum) VALUES (%s, %s);".format(self.TABLE_WITH_TRANSACTIONS)
        self.db.execute(create_query, (transaction_id, transaction_value))
        self.db.commit()

    def apply_sales(self, transaction_id):
        apply_query = "UPDATE {} SET sum = (SELECT sum FROM {} WHERE id = %s) * 0.1 WHERE id = %s".format(self.TABLE_WITH_TRANSACTIONS, self.TABLE_WITH_TRANSACTIONS)
        self.db.execute(apply_query, (transaction_id, transaction_id))
        self.db.commit()

    def _add_item(self, table_name, data, headers):
        # First column with id will be ignored
        headers = [str(header[0]) for header in headers]
        data_placeholders = ", ".join(["%s"] * len(data))
        headers = ", ".join(headers)

        self.db.connect()
        self.db.execute("INSERT INTO {} ({}) VALUES ({})".format(table_name, headers, data_placeholders), data)
        self.db.commit()
        self.db.disconnect()

    def edit(self):
        selection_ids = self._get_selection_ids()
        if not selection_ids:
            return # TODO: Add warning about empty selection

        size = self.table_widget.columnCount() - 1, self.table_widget.rowCount() - 1

        values = []
        dialog = AddingDialog(size, self.headers[1:], values)

        if dialog.exec():
            values = [v for v in values if v]

            for item_id in selection_ids:
                self._edit_item(self.active_table, values, self.headers[1:], item_id)
            self.refresh()

    def _edit_item(self, table_name, data, headers, selection_id):
        update_data = []
        headers = [str(header[0]) for header in headers]
        for header, value in zip(headers, data):
            if not value:
                continue
            update_data.append("{} = %s".format(header))

        update_data = ", ".join(update_data)

        self.db.connect()
        self.db.execute("UPDATE {} SET {} WHERE id = {}".format(table_name, update_data, selection_id), data)
        self.db.commit()
        self.db.disconnect()

    def _get_selection_ids(self):
        items = self.table_widget.selectedItems()
        ids = []
        for item in items:
            ids.append(int(self.table_widget.item(item.row(), 0).text()))

        return ids

    def remove(self):
        selection_ids = self._get_selection_ids()
        if not selection_ids:
            return # TODO: Add warning about empty selection

        button = QMessageBox.question(self, "Deletion", "Do you want to delete a record?")

        if button == QMessageBox.Yes:
            for item_id in selection_ids:
                self._remove_item(self.active_table, item_id)
            self.refresh()

    def _remove_item(self, table_name, item_id):
        self.db.connect()
        self.db.execute("DELETE FROM {} WHERE id = {}".format(table_name, item_id))
        self.db.commit()
        self.db.disconnect()
