from bin.db import DBManager
from bin.gui.entry_edit_widget import EntryEditWidget
from bin.gui.page_counter_widget import PageCounterWidget
from bin.gui.adding_dialog import AddingDialog
from bin.gui.rent_adding_dialog import RentAdding

from PySide6.QtCore import QSize
from PySide6.QtWidgets import (
    QMainWindow, QWidget, QMessageBox,
    QVBoxLayout, QHBoxLayout, QTableWidget,
    QTableWidgetItem, QToolBar, QFileDialog
)

from PySide6.QtGui import QAction

import os
from functools import partial

from tabulate import tabulate


class TablesViewer(QMainWindow):
    """GUI allowing to view and edit tables data"""

    DB_NAME = "test_db"
    USER = "test"

    MAX_ROWS = 5
    TABLES = [
        "rooms", "clients", "rents", "transactions", "clients_rents", "sales"
    ]

    def __init__(self):
        super().__init__()

        self.setFixedSize(QSize(800, 450))

        self.db = DBManager(self.DB_NAME, self.USER)

        self.table_widget = QTableWidget()
        self.entry_edit_widget = EntryEditWidget(
            self.add, self.remove, self.edit, self.save_active_table, self.save_all_tables
        )
        self.page_counter = PageCounterWidget(self.refresh)

        toolbar = QToolBar("Tables Toolbar")
        self.addToolBar(toolbar)

        self.tables_switching_actions = [
            QAction("Rooms"),
            QAction("Clients"),
            QAction("Rents"),
            QAction("Transactions"),
            QAction("Clients/Rents"),
            QAction("Sales"),
        ]
        for action, table in zip(self.tables_switching_actions, self.TABLES):
            action.triggered.connect(partial(self.show_table, table))
            toolbar.addAction(action)

        layout = QVBoxLayout()
        layout_for_table = QHBoxLayout()

        layout_for_table.addWidget(self.table_widget)
        layout_for_table.addWidget(self.entry_edit_widget)
        layout.addLayout(layout_for_table)
        layout.addWidget(self.page_counter)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

        self.current_page = 1
        self.active_table = self.TABLES[0]

    def refresh(self):
        self.show_table(self.active_table)

    def show_table(self, table_name):
        headers = self._get_headers(table_name)
        data = self._get_data(table_name)

        self._init_pages(len(data))
        self._show_data(data)
        self.page_counter.update()
        self._set_headers(headers)

        self.active_table = table_name

    def _get_headers(self, table_name):
        query = "SELECT column_name FROM information_schema.columns WHERE table_name = '{}'".format(table_name)

        return self.db.execute_and_return(query)

    def _get_data(self, table_name):
        query = "SELECT * FROM {}".format(table_name)

        return self.db.execute_and_return(query)

    def _init_pages(self, records):
        if records <= self.MAX_ROWS:
            total_pages = 1
        else:
            total_pages = records // self.MAX_ROWS
            if records % self.MAX_ROWS:
                total_pages += 1

        if self.page_counter.total_pages != total_pages:
            self.page_counter.init_pages(total_pages)

    def _show_data(self, data):
        if not data:
            QMessageBox.information(self, "Empty Table", "This table is empty")
            return

        records_remainder = len(data) % self.MAX_ROWS

        if self.page_counter.current_page == self.page_counter.total_pages and records_remainder:
            rows = records_remainder
        else:
            rows = self.MAX_ROWS

        self.table_widget.setRowCount(rows)
        self.table_widget.setColumnCount(len(data[0]))

        start = self.MAX_ROWS * (self.page_counter.current_page - 1)
        end = self.MAX_ROWS * (self.page_counter.current_page)

        if len(data) > self.MAX_ROWS:
            data = data[start:end]

        for x in range(len(data)):
            for y in range(len(data[0])):
                item = QTableWidgetItem(str(data[x][y]))
                self.table_widget.setItem(x, y, item)

    def _set_headers(self, headers):
        self.headers = headers
        self.table_widget.setHorizontalHeaderLabels([header[0] for header in headers])

    def add(self):
        self.db.connect()

        collected_data = []
        if self.headers[0][0] == "id":
            size = len(self.headers) - 1, 1
            if self.active_table == "rents":
                dialog = RentAdding(self.db)
            else:
                dialog = AddingDialog(size, self.headers[1:], collected_data)
        else:
            size = len(self.headers), 1
            dialog = AddingDialog(size, self.headers[:], collected_data)

        if not dialog.exec():
            return

        if self.active_table != "rents":
            self._add_item(self.active_table, collected_data, self.headers[1:])
        self.refresh()

        self.db.disconnect()

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

    def save_active_table(self):
        dialog = QFileDialog()
        file_name, status = dialog.getSaveFileName(self, "Save File", ".", "*.txt")

        try:
            self._save_table(file_name, self.active_table)
        except Exception:
            pass
        else:
            QMessageBox.information(self, "Succes", "Table succesfully saved")

    def save_all_tables(self):
        dialog = QFileDialog()
        folder_name, status = dialog.getSaveFileName(self, "Save Folder", ".", "")

        try:
            os.mkdir(folder_name)
            for table in self.TABLES:
                self._save_table(os.path.join(folder_name, table + ".txt"), table)
        except Exception:
            pass
        else:
            QMessageBox.information(self, "Succes", "Tables succesfully saved")

    def _save_table(self, file_name, table_name):
        headers = [header[0] for header in self._get_headers(table_name)]
        data = self._get_data(table_name)

        table = tabulate(data, headers=headers, tablefmt="github")

        with open(file_name, "w") as file:
            file.write(table)
