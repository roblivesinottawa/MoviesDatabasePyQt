from PyQt5.QtCore import Qt
from PyQt5.QtSql import QSqlTableModel


class MoviesModel:
    def __init__(self):
        self.model = self._createModel()

    @staticmethod
    def _createModel():
        tableModel = QSqlTableModel()
        tableModel.setTable("movies")
        tableModel.setEditStrategy(QSqlTableModel.OnFieldChange)
        tableModel.select()
        headers = ("ID", "Title", "Year", "Email")
        for columnIndex, header in enumerate(headers):
            tableModel.setHeaderData(columnIndex, Qt.Horizontal, header)
        return tableModel

    def addMovie(self, data):
        # ADD A MOVIE TO THE DATABASE
        rows = self.model.rowCount()
        self.model.insertRows(rows, 1)
        for column, field in enumerate(data):
            self.model.setData(self.model.index(rows, column + 1), field)
        self.model.submitAll()
        self.model.select()

    def deleteContact(self, row):
        # remove a movie from the database
        self.model.removeRow(row)
        self.model.submitAll()
        self.model.select()

    def clearContacts(self):
        self.model.editStrategy(QSqlTableModel.OnManualSubmit)
        self.model.removeRows(0, self.model.rowCount())
        self.model.submitAll()
        self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.model.select()