import sqlite3
from PyQt5.QtWidgets import QApplication, QTableView
from PyQt5.QtSql import QSqlTableModel, QSqlDatabase
import os.path
# Create a connection to the SQLite database
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_dir = (BASE_DIR + '\\inverted_index.db')
conn = sqlite3.connect(db_dir)

# Create a QSqlDatabase object to handle the connection
db = QSqlDatabase.addDatabase('QSQLITE')
db.setDatabaseName('database.db')
db.open()

# Create a QSqlTableModel object to display the data in a QTableView widget
model = QSqlTableModel()
model.setTable('tablename')
model.select()

# Get the column names from the model
columns = [model.headerData(i, 1) for i in range(model.columnCount())]

# Display the column names in the console
print(columns)

# Create a QTableView widget to display the data
app = QApplication([])
view = QTableView()
view.setModel(model)
view.show()
app.exec_()
