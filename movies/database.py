from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtSql import QSqlDatabase, QSqlQuery


def _createMoviesTable():
    createTableQuery = QSqlQuery()
    return createTableQuery.exec(
        """
        CREATE TABLE IF NOT EXISTS movies (
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
        title VARCHAR(40) NOT NULL,
        year INTEGER(11) NOT NULL,
        country VARCHAR(40) NOT NULL
        )
        """
    )


def createConnection(dbname):
    connection = QSqlDatabase.addDatabase("QSQLITE")
    connection.setDatabaseName(dbname)

    if not connection.open():
        QMessageBox.warning(
            None,
            "Movies",
            f"Database Error: {connection.lastError().text()}"
        )
        return False
    _createMoviesTable()
    return True
