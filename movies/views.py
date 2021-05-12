# -*- coding: utf-8 -*-

"""This module provides views to manage the movies table."""
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QAbstractItemView,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QHBoxLayout,
    QLineEdit,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QTableView,
    QVBoxLayout,
    QWidget,
)
from .model import MoviesModel


class Window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Movies Database")
        self.resize(550, 250)
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.layout = QHBoxLayout()
        self.centralWidget.setLayout(self.layout)
        self.moviesModel = MoviesModel()
        self.setupUI()

    def setupUI(self):
        # create the table view
        self.table = QTableView()
        self.table.setModel(self.moviesModel.model)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.resizeColumnsToContents()
        # create buttons
        self.addButton = QPushButton("Add...")
        self.addButton.clicked.connect(self.openAddDialog)
        self.deleteButton = QPushButton("Delete...")
        self.deleteButton.clicked.connect(self.deleteMovie)
        self.clearAllButton = QPushButton("Clear All...")
        self.clearAllButton.clicked.connect(self.clearMovies)
        # lay out the GUI
        layout = QVBoxLayout()
        layout.addWidget(self.addButton)
        layout.addWidget(self.deleteButton)
        layout.addStretch()
        layout.addWidget(self.clearAllButton)
        self.layout.addWidget(self.table)
        self.layout.addLayout(layout)

    def openAddDialog(self):
        # opens the add movie dialog
        dialog = AddDialog(self)
        if dialog.exec() == QDialog.Accepted:
            self.moviesModel.addMovie(dialog.data)
            self.table.resizeColumnsToContents()

    def deleteMovie(self):
        """remove the selected movie from the window"""
        row = self.table.currentIndex().row()
        if row < 0:
            return

        messageBox = QMessageBox.warning(
            self,
            "Warning!",
            f"Do you want to remove the selected movie?",
            QMessageBox.Ok | QMessageBox.Cancel,
        )

        if messageBox == QMessageBox.Ok:
            self.moviesModel.deleteContact(row)

    def clearMovies(self):
        """remove all movies from the database"""
        messageBox = QMessageBox.warning(
            self,
            "Warning!",
            f"Do you want to remove all the movies?",
            QMessageBox.Ok | QMessageBox.Cancel,
        )

        if messageBox == QMessageBox.Ok:
            self.moviesModel.clearContacts()


class AddDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setWindowTitle("Add Movie")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.data = None

        self.setupUI()

    def setupUI(self):
        # create line edits for data fields
        self.titleField = QLineEdit()
        self.titleField.setObjectName("Title")
        self.yearField = QLineEdit()
        self.yearField.setObjectName("Year")
        self.countryField = QLineEdit()
        self.countryField.setObjectName("Country")

        # lay out the data fields
        layout = QFormLayout()
        layout.addRow("Title:", self.titleField)
        layout.addRow("Year:", self.yearField)
        layout.addRow("Country:", self.countryField)
        self.layout.addLayout(layout)

        # add standard buttons to the dialog and connect them
        self.buttonsBox = QDialogButtonBox(self)
        self.buttonsBox.setOrientation(Qt.Horizontal)
        self.buttonsBox.setStandardButtons(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        )
        self.buttonsBox.accepted.connect(self.accept)
        self.buttonsBox.rejected.connect(self.reject)
        self.layout.addWidget(self.buttonsBox)

    def accept(self):
        self.data = []
        for field in (self.titleField, self.yearField, self.countryField):
            if not field.text():
                QMessageBox.critical(
                    self,
                    "Error!",
                    f"You must provide a movie's {field.objectName()}",
                )
                self.data = None  # this resets data
                return

            self.data.append(field.text())

        if not self.data:
            return

        super().accept()
