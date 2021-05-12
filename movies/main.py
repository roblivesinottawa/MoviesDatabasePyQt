# -*- coding: utf-8 -*-
# movies_gui/main.py

""" This module provides Movies Database Application """

import sys
from PyQt5.QtWidgets import QApplication
from .database import createConnection
from .views import Window


def main():
    """movies database main function"""
    app = QApplication(sys.argv)
    # connect to the database
    if not createConnection("movies.sqlite"):
        sys.exit(1)
    win = Window()
    win.show()
    sys.exit(app.exec())
