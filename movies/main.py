# -*- coding: utf-8 -*-
# movies_gui/main.py

""" This module provides Movies Database Application """

import sys
from PyQt5.QtWidgets import QApplication
from .views import Window

def main():
    """movies database main function"""
    app = QApplications(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())
