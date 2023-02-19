from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import os.path

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1065, 773)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("supermarket")
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1065, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        # Call method to populate table with data from database
        self.populate_table()

    def populate_table(self):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_dir = (BASE_DIR + '\\inverted_index.db')
        # Connect to database and execute SELECT statement
        conn = sqlite3.connect(db_dir)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM words')
        data = cursor.fetchall()

        # Set column and row count for table
        self.tableWidget.setColumnCount(len(data[0]))
        self.tableWidget.setRowCount(len(data))

        # Insert data into table
        for row in range(len(data)):
            for col in range(len(data[0])):
                self.tableWidget.setItem(row, col, QtWidgets.QTableWidgetItem(str(data[row][col])))

        # Close database connection
        conn.close()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Scrap DATA"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

