from abc import ABCMeta, abstractmethod

from PySide6.QtWidgets import QWidget


class Controller(QWidget):
    __metaclass__ = ABCMeta

    @abstractmethod
    def data_check(self):
        """Check data on logical corectness, return bool, raise exceptions"""

    @abstractmethod
    def create(self):
        """Initialise corresponding model with data"""
