import sqlite3
from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem

conn = sqlite3.connect('C:/Users/Nattavee Narischat/Desktop/softdev2/Week12/inverted_index.db')
cur = conn.cursor()

cur.execute('SELECT Link,Title,Body,Location FROM documents')
data = cur.fetchall()

cur.execute("PRAGMA table_info(documents)")
schema = cur.fetchall()

app = QApplication([])
table = QTableWidget()

table.setRowCount(len(data))
table.setColumnCount(len(schema))

for i, column in enumerate(schema):
    name = column[1]
    item = QTableWidgetItem(name)
    table.setHorizontalHeaderItem(i, item)

for i, row in enumerate(data):
    for j, value in enumerate(row):
        item = QTableWidgetItem(str(value))
        table.setItem(i, j, item)

table.show()
app.exec_()
