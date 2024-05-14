from abc import ABCMeta, abstractmethod

from PySide6.QtWidgets import QWidget


class Controller(QWidget):
    """Used with tables viewer for data collection and model init if neccesary."""

    @abstractmethod
    def data_check(self, *args, **kwargs):
        """Check data on logical corectness, return bool, raise exceptions"""

    @abstractmethod
    def create(self, *args, **kwargs):
        """Initialise corresponding model with data"""
