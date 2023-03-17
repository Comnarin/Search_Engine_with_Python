

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QInputDialog, QLineEdit, QListWidgetItem, QMessageBox,QFileDialog,QHeaderView
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5 import QtCore, QtGui, QtWidgets

import locationtagger
import pythainlp.util
from pythainlp.summarize import summarize
from urllib.parse import urljoin
import time
from pythainlp.tag import tag_provinces
from pythainlp.tokenize import word_tokenize as tokenizer

from datetime import datetime
import math
import requests
from bs4 import BeautifulSoup
import time
from urllib.parse import urljoin
import sqlite3

import spacy
from spacy.tokenizer import Tokenizer
from spacy.lang.en import English



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 875)
        MainWindow.setMinimumSize(QtCore.QSize(800, 700))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.tabWidget_edit = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget_edit.setMinimumSize(QtCore.QSize(640, 480))
        self.tabWidget_edit.setObjectName("tabWidget_edit")
        self.tab_scrapping = QtWidgets.QWidget()
        self.tab_scrapping.setMouseTracking(False)
        self.tab_scrapping.setAccessibleName("")
        self.tab_scrapping.setAutoFillBackground(False)
        self.tab_scrapping.setObjectName("tab_scrapping")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_scrapping)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_Queue = QtWidgets.QLabel(self.tab_scrapping)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_Queue.setFont(font)
        self.label_Queue.setObjectName("label_Queue")
        self.horizontalLayout.addWidget(self.label_Queue)
        self.label_Depth = QtWidgets.QLabel(self.tab_scrapping)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_Depth.setFont(font)
        self.label_Depth.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_Depth.setObjectName("label_Depth")
        self.horizontalLayout.addWidget(self.label_Depth)
        self.spinBox_Depth = QtWidgets.QSpinBox(self.tab_scrapping)
        self.spinBox_Depth.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.spinBox_Depth.setFont(font)
        self.spinBox_Depth.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.spinBox_Depth.setReadOnly(False)
        self.spinBox_Depth.setKeyboardTracking(True)
        self.spinBox_Depth.setSuffix("")
        self.spinBox_Depth.setMinimum(1)
        self.spinBox_Depth.setObjectName("spinBox_Depth")
        self.horizontalLayout.addWidget(self.spinBox_Depth)
        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.save_path = QtWidgets.QPushButton(self.tab_scrapping)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.save_path.setFont(font)
        self.save_path.setObjectName("save_path")
        self.verticalLayout_2.addWidget(self.save_path)
        self.label_Input_domain = QtWidgets.QLabel(self.tab_scrapping)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setUnderline(True)
        self.label_Input_domain.setFont(font)
        self.label_Input_domain.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_Input_domain.setObjectName("label_Input_domain")
        self.verticalLayout_2.addWidget(self.label_Input_domain)
        self.listWidget = QtWidgets.QListWidget(self.tab_scrapping)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.listWidget.setFont(font)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_2.addWidget(self.listWidget)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.Button_OpenQueue = QtWidgets.QPushButton(self.tab_scrapping)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Button_OpenQueue.setFont(font)
        self.Button_OpenQueue.setObjectName("Button_OpenQueue")
        self.verticalLayout_5.addWidget(self.Button_OpenQueue)
        self.Button_PAUSE = QtWidgets.QPushButton(self.tab_scrapping)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Button_PAUSE.setFont(font)
        self.Button_PAUSE.setObjectName("Button_PAUSE")
        self.verticalLayout_5.addWidget(self.Button_PAUSE)
        self.Button_RESUME = QtWidgets.QPushButton(self.tab_scrapping)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Button_RESUME.setFont(font)
        self.Button_RESUME.setObjectName("Button_RESUME")
        self.verticalLayout_5.addWidget(self.Button_RESUME)
        self.gridLayout_2.addLayout(self.verticalLayout_5, 5, 1, 1, 1)
        self.path_file = QtWidgets.QLabel(self.tab_scrapping)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.path_file.setFont(font)
        self.path_file.setObjectName("path_file")
        self.gridLayout_2.addWidget(self.path_file, 6, 0, 1, 1)
        self.Button_Index = QtWidgets.QPushButton(self.tab_scrapping)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Button_Index.setFont(font)
        self.Button_Index.setObjectName("Button_Index")
        self.gridLayout_2.addWidget(self.Button_Index, 6, 1, 1, 1)

        self.list_queue = QtWidgets.QListWidget(self.tab_scrapping)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.list_queue.setFont(font)
        self.list_queue.setObjectName("listWidget_Queue")
        
        self.gridLayout_2.addWidget(self.list_queue, 3, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_Total = QtWidgets.QLabel(self.tab_scrapping)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_Total.setFont(font)
        self.label_Total.setObjectName("label_Total")
        self.horizontalLayout_2.addWidget(self.label_Total)
        self.lcdNumber = QtWidgets.QLCDNumber(self.tab_scrapping)
        self.lcdNumber.setObjectName("lcdNumber")
        self.horizontalLayout_2.addWidget(self.lcdNumber)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 4, 0, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.textBrowser = QtWidgets.QTextBrowser(self.tab_scrapping)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_4.addWidget(self.textBrowser)
        self.progressBar = QtWidgets.QProgressBar(self.tab_scrapping)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.progressBar.setFont(font)
        self.progressBar.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_4.addWidget(self.progressBar)
        self.gridLayout_2.addLayout(self.verticalLayout_4, 5, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, 50, -1, -1)
        self.verticalLayout.setSpacing(30)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.Button_ADD = QtWidgets.QPushButton(self.tab_scrapping)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Button_ADD.setFont(font)
        self.Button_ADD.setObjectName("Button_ADD")
        self.verticalLayout.addWidget(self.Button_ADD)
        self.Button_EDIT = QtWidgets.QPushButton(self.tab_scrapping)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Button_EDIT.setFont(font)
        self.Button_EDIT.setObjectName("Button_EDIT")
        self.verticalLayout.addWidget(self.Button_EDIT)
        self.Button_REMOVE = QtWidgets.QPushButton(self.tab_scrapping)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Button_REMOVE.setFont(font)
        self.Button_REMOVE.setObjectName("Button_REMOVE")
        self.verticalLayout.addWidget(self.Button_REMOVE)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 1, 1, 1)
        self.Button_CRAWLER = QtWidgets.QPushButton(self.tab_scrapping)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Button_CRAWLER.setFont(font)
        self.Button_CRAWLER.setIconSize(QtCore.QSize(16, 16))
        self.Button_CRAWLER.setAutoDefault(False)
        self.Button_CRAWLER.setDefault(False)
        self.Button_CRAWLER.setFlat(False)
        self.Button_CRAWLER.setObjectName("Button_CRAWLER")
        self.gridLayout_2.addWidget(self.Button_CRAWLER, 3, 1, 1, 1)
        self.tabWidget_edit.addTab(self.tab_scrapping, "")
        self.tab_Search = QtWidgets.QWidget()
        self.tab_Search.setObjectName("tab_Search")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_Search)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Button_view_path = QtWidgets.QPushButton(self.tab_Search)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Button_view_path.setFont(font)
        self.Button_view_path.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Button_view_path.setObjectName("Button_view_path")
        self.verticalLayout_3.addWidget(self.Button_view_path)
        self.splitter = QtWidgets.QSplitter(self.tab_Search)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.Search_input = QtWidgets.QTextEdit(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Search_input.setFont(font)
        self.Search_input.setObjectName("Search_input")
        self.Search_button = QtWidgets.QPushButton(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(40)
        self.Search_button.setFont(font)
        self.Search_button.setObjectName("Search_button")
        self.verticalLayout_3.addWidget(self.splitter)
        self.label_data = QtWidgets.QLabel(self.tab_Search)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_data.setFont(font)
        self.label_data.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_data.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_data.setObjectName("label_data")
        self.verticalLayout_3.addWidget(self.label_data)
        self.table_showDatabase = QtWidgets.QTableWidget(self.tab_Search)
        self.table_showDatabase.setObjectName("table_showDatabase")
        self.table_showDatabase.setColumnCount(0)
        self.table_showDatabase.setRowCount(0)
        self.verticalLayout_3.addWidget(self.table_showDatabase)
        self.verticalLayout_3.setStretch(1, 1)
        self.verticalLayout_3.setStretch(3, 10)
        self.tabWidget_edit.addTab(self.tab_Search, "")
        self.tab_edit = QtWidgets.QWidget()
        self.tab_edit.setObjectName("tab_edit")
        self.gridLayout = QtWidgets.QGridLayout(self.tab_edit)
        self.gridLayout.setHorizontalSpacing(1)
        self.gridLayout.setVerticalSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.textEdit_Update = QtWidgets.QTextEdit(self.tab_edit)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.textEdit_Update.setFont(font)
        self.textEdit_Update.setObjectName("textEdit_Update")
        self.gridLayout.addWidget(self.textEdit_Update, 1, 2, 1, 1)
        self.Button_update = QtWidgets.QPushButton(self.tab_edit)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Button_update.setFont(font)
        self.Button_update.setObjectName("Button_update")
        self.gridLayout.addWidget(self.Button_update, 1, 4, 1, 1)
        self.progressBar_Update = QtWidgets.QProgressBar(self.tab_edit)
        self.progressBar_Update.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Kenya))
        self.progressBar_Update.setProperty("value", 24)
        self.progressBar_Update.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar_Update.setObjectName("progressBar_Update")
        self.gridLayout.addWidget(self.progressBar_Update, 2, 2, 1, 1)
        self.textEdit_Remove = QtWidgets.QTextEdit(self.tab_edit)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.textEdit_Remove.setFont(font)
        self.textEdit_Remove.setObjectName("textEdit_Remove")
        self.gridLayout.addWidget(self.textEdit_Remove, 4, 1, 1, 2)
        self.Button_Remove = QtWidgets.QPushButton(self.tab_edit)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Button_Remove.setFont(font)
        self.Button_Remove.setObjectName("Button_Remove")
        self.gridLayout.addWidget(self.Button_Remove, 4, 4, 1, 1)
        self.textBrowser_Console_Edit = QtWidgets.QTextBrowser(self.tab_edit)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.textBrowser_Console_Edit.setFont(font)
        self.textBrowser_Console_Edit.setObjectName("textBrowser_Console_Edit")
        self.gridLayout.addWidget(self.textBrowser_Console_Edit, 6, 0, 1, 3)
        self.progressBar_Remove = QtWidgets.QProgressBar(self.tab_edit)
        self.progressBar_Remove.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.progressBar_Remove.setProperty("value", 24)
        self.progressBar_Remove.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar_Remove.setObjectName("progressBar_Remove")
        self.gridLayout.addWidget(self.progressBar_Remove, 5, 1, 1, 2)
        self.label_Remove = QtWidgets.QLabel(self.tab_edit)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_Remove.setFont(font)
        self.label_Remove.setObjectName("label_Remove")
        self.gridLayout.addWidget(self.label_Remove, 3, 2, 1, 1)
        self.label_UPDATE = QtWidgets.QLabel(self.tab_edit)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_UPDATE.setFont(font)
        self.label_UPDATE.setObjectName("label_UPDATE")
        self.gridLayout.addWidget(self.label_UPDATE, 0, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 3, 1, 1)
        self.gridLayout.setColumnStretch(2, 10)
        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 1)
        self.gridLayout.setRowStretch(2, 1)
        self.gridLayout.setRowStretch(3, 1)
        self.gridLayout.setRowStretch(4, 1)
        self.gridLayout.setRowStretch(6, 30)
        self.tabWidget_edit.addTab(self.tab_edit, "")
        self.tab_Visualization = QtWidgets.QWidget()
        self.tab_Visualization.setObjectName("tab_Visualization")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_Visualization)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_Spatial = QtWidgets.QLabel(self.tab_Visualization)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_Spatial.setFont(font)
        self.label_Spatial.setObjectName("label_Spatial")
        self.gridLayout_5.addWidget(self.label_Spatial, 0, 0, 1, 1)
        self.graphicsView_spatial = QtWidgets.QGraphicsView(self.tab_Visualization)
        self.graphicsView_spatial.setObjectName("graphicsView_spatial")
        self.gridLayout_5.addWidget(self.graphicsView_spatial, 1, 0, 1, 1)
        self.label_Topkeywords = QtWidgets.QLabel(self.tab_Visualization)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_Topkeywords.setFont(font)
        self.label_Topkeywords.setObjectName("label_Topkeywords")
        self.gridLayout_5.addWidget(self.label_Topkeywords, 2, 0, 1, 1)
        self.graphicsView_Keyword = QtWidgets.QGraphicsView(self.tab_Visualization)
        self.graphicsView_Keyword.setObjectName("graphicsView_Keyword")
        self.gridLayout_5.addWidget(self.graphicsView_Keyword, 3, 0, 1, 1)
        self.tabWidget_edit.addTab(self.tab_Visualization, "")
        self.gridLayout_4.addWidget(self.tabWidget_edit, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget_edit.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.Button_ADD.clicked.connect(self.Addlinks)
        self.load_input_domain()
        self.Button_EDIT.clicked.connect(self.editlinks)
        self.Button_REMOVE.clicked.connect(self.removelink)
        self.Button_CRAWLER.clicked.connect(self.clicked_start)
        self.save_path.clicked.connect(self.openFileSave)
        self.Button_Index.setEnabled(False)
        self.folderpath = None
        self.textBrowser.append("Please Select directory")
        self.Button_CRAWLER.setEnabled(False)
        self.Button_PAUSE.setEnabled(False)
        self.Button_RESUME.setEnabled(False)

        self.Button_view_path.clicked.connect(self.openFileNameDialog)
        self.Search_button.clicked.connect(self.search_input)

    def load_input_domain(self):
        domainlinks = ['http://www.bbc.com','http://www.thairath.co.th']
        for i in domainlinks:
            self.listWidget.addItem(i)
        self.listWidget.setCurrentRow(0)

    def Addlinks(self):
        currentIndex = self.listWidget.currentRow()
        text, ok = QInputDialog.getText(MainWindow,"New Link","Link Name")
        if ok and text is not None:
            self.listWidget.insertItem(currentIndex,text)
    
    def editlinks(self):
        currentIndex = self.listWidget.currentRow()
        item = self.listWidget.item(currentIndex)
        if item is not None:
            text, ok = QInputDialog.getText(MainWindow,"Edit Link","Link Name",QLineEdit.Normal,item.text())
            if text and ok is not None:
                item.setText(text)

    def removelink(self):
        currentIndex = self.listWidget.currentRow()
        item = self.listWidget.item(currentIndex)
        if item is None:
            return

        question = QMessageBox.question(MainWindow,"Remove Link",
                                        "Do you want to remove Link ?  \n" + item.text(),
                                        QMessageBox.Yes | QMessageBox.No)

        if question == QMessageBox.Yes:
            item = self.listWidget.takeItem(currentIndex)
            del item

    def clicked_start(self):
        
        self.textBrowser.clear()
        
        self.Button_CRAWLER.setEnabled(False)
        self.Button_ADD.setEnabled(False)
        self.Button_EDIT.setEnabled(False)
        self.Button_REMOVE.setEnabled(False)
        self.Button_RESUME.setEnabled(False)
        self.Button_OpenQueue.setEnabled(False)
        self.Button_PAUSE.setEnabled(False)
        self.Button_Index.setEnabled(False)
         
        self.textBrowser.append("Starting Scrap ..........")
        self.progressBar.setProperty("value", 10)
        global target_links 
        target_links = []
        for i in range(self.listWidget.count()):
            item = self.listWidget.item(i)
            target_links.append(item.text())
        self.Craw_Domain()
        depth_value = self.spinBox_Depth.value()

        
        self.thread = SpiderThread(target_links, depth_value)
        self.progressBar.setProperty("value", 20)
        self.thread.progress_signal.connect(self.progress_ui)
        self.progressBar.setProperty("value", 25)
        self.thread.count_links_signal.connect(self.count_links_scraping)
        self.thread.each_links_finished.connect(self.update_label)
        
        #self.thread.count_signal.connect(self.update_lcd)
        self.thread.finished.connect(self.update_ui)
        self.thread.finished.connect(lambda: self.Button_Index.setEnabled(True))
        self.thread.start()

    def Craw_Domain(self):
        conn = sqlite3.connect(db_dir)
        for j in target_links:
            domain = conn.execute("SELECT id FROM domain_link  WHERE domain_link  = ?", (j,)).fetchone()
            if not domain:
                conn.execute("INSERT INTO domain_link (domain_link) VALUES (?)", (j,))
                conn.commit()

    def count_links_scraping(self,each_links_finished):
        #self.lcdNumber.display(count_links) 
        self.lcdNumber.display(each_links_finished[0])
        self.label_Total.setText(each_links_finished[1])

    def update_label(self, count):
        #percent = 100*(count/len(target_links))-25
        percent = (100*((count)/len(target_links)))
        self.progressBar.setProperty("value", percent)
        



    def progress_ui(self,i):
        #self.textBrowser.clear()
        self.textBrowser.append(i)
        

    def update_ui(self, domain_links):
        self.textBrowser.clear()
        self.scrap_links = domain_links
        for i in self.scrap_links:
            self.textBrowser.append(i)
        self.lcdNumber.display(len(domain_links))
        self.label_Total.setText("Total")
        self.progressBar.setProperty("value", 100)
        self.Button_Index.clicked.connect(self.clicked_Index)
        self.Button_Index.setEnabled(True)

            
    def openFileSave(self):
        while True:
                self.path_file.setText("No directory selected")
                self.folderpath = QtWidgets.QFileDialog.getExistingDirectory(MainWindow, 'Select Folder')
                if self.folderpath:
                    break
        self.path_file.setText("Save as: " + self.folderpath)
        global db_dir
        db_dir = (self.folderpath+'/inverted_index.db')
        self.textBrowser.clear()
        self.textBrowser.append("Create Database")
        self.create_db(db_dir)
        self.Button_CRAWLER.setEnabled(True)
        self.Button_PAUSE.setEnabled(True)
        self.Button_RESUME.setEnabled(True)
        self.save_path.setEnabled(False)
        self.textBrowser.clear()
        self.textBrowser.append("Create Database Success")

    def create_db(self,db_dir):
        
        conn = sqlite3.connect(db_dir)

        # Create tables for words, documents, and word frequencies

        conn.execute('''
        CREATE TABLE words (
            ID INTEGER PRIMARY KEY,
            Word TEXT NOT NULL UNIQUE
        );
        ''')

        conn.execute('''
        CREATE TABLE documents (
            ID INTEGER PRIMARY KEY,
            Link TEXT NOT NULL UNIQUE ,
            Title TEXT,
            Body TEXT,
            Location TEXT,
            Ref INT,
            Time TEXT
        );
        ''')

        conn.execute('''
        CREATE TABLE word_frequencies (
            Word_ID INTEGER ,
            Doc_ID INTEGER ,
            Frequency INTEGER NOT NULL,
            TF_IDF REAL ,
            PRIMARY KEY (word_id, doc_id),
            FOREIGN KEY (word_id) REFERENCES words(id),
            FOREIGN KEY (doc_id) REFERENCES documents(id)
        );
        ''')
        conn.execute('''
        CREATE TABLE Temp_link(
            ID INTEGER PRIMARY KEY,
            Link TEXT NOT NULL UNIQUE
        );
        ''')

        conn.execute('''
        CREATE TABLE Domain_link(
            ID INTEGER PRIMARY KEY,
            Domain_Link TEXT NOT NULL UNIQUE
        );
        ''')
        conn.commit()

    def clicked_Index(self):
        self.textBrowser.clear()
        if not self.folderpath:
            QMessageBox.information(MainWindow, 'No Directory Selected', 'Please select a directory')
            self.folderpath = QtWidgets.QFileDialog.getExistingDirectory(MainWindow, 'Select Folder')
            if self.folderpath:
                self.path_file.setText("Save as: " + self.folderpath)
                global db_dir
                db_dir = (self.folderpath+'/inverted_index.db')
                self.textBrowser.append("Create Database")
                self.create_db(db_dir)

                self.save_path.setEnabled(False)
                self.textBrowser.clear()
                self.textBrowser.append("Create Database Success")
            else:
                while True:
                    self.path_file.setText("No directory selected")
                    self.folderpath = QtWidgets.QFileDialog.getExistingDirectory(MainWindow, 'Select Folder')
                    if self.folderpath:
                        break
        self.save_path.setEnabled(False)
        self.textBrowser.clear()
        self.textBrowser.append("Adding Database")
        self.addlinks_into_database()
        self.textBrowser.clear()
        self.textBrowser.append("Indexing")


    def addlinks_into_database(self):
        conn = sqlite3.connect(db_dir)
        links = self.scrap_links
        domain = conn.execute('select domain_link from domain_link').fetchall()
        domain = [t[0] for t in domain]
        for i in links :
            for j in domain:
                if i.startswith(j):
                    conn.execute('''INSERT INTO Temp_link (Link) VALUES (?);''', (i,))
                    conn.commit()
        self.show_queue()
        self.temp_to_index()

    def show_queue(self):
        self.textBrowser.clear()
        conn = sqlite3.connect(db_dir)
        cursor = conn.cursor()
        cursor.execute('SELECT Link FROM Temp_link')
        #try:
            #cursor.execute('SELECT * FROM documents')
        #except:
            #print("It's is not my database")
        Temp_link = cursor.fetchall()
        Temp_link = [t[0] for t in Temp_link]
        # Insert data into table
        

        for i in Temp_link:
            self.list_queue.addItem(i)

        self.textBrowser.append("Database is showing")
        # Close database connection
        conn.close()

    def temp_to_index(self):
        conn = sqlite3.connect(db_dir)
        links = conn.execute('SELECT Link FROM temp_link ').fetchall()
        links = [t[0] for t in links]
        ref=self.get_ref()
        for i in links:
            doc = self.make_doc(i,ref)
            print(doc)
            self.insert_to_database([doc])
            conn.execute('DELETE FROM temp_link WHERE link = ?; ', (i,))
            conn.commit()

    def insert_to_database(self,doc):
        conn = sqlite3.connect(db_dir)
        for i in doc:
            conn.execute('''INSERT INTO documents (Link, Title, Body, Location, Ref, Time) VALUES (?, ?, ?, ?, ?, ?);''', (str(i['link']), str(i['title']), str(i['body']), str(i['location']), int(i['ref']), datetime.now()))
            doc_id = conn.execute("SELECT last_insert_rowid()").fetchone()[0]
            
            for j in i['word'].keys():
                word_id = conn.execute("SELECT id FROM words WHERE word = ?", (j,)).fetchone()
                if not word_id:
                    conn.execute("INSERT INTO words (word) VALUES (?)", (j,))
                    word_id = conn.execute("SELECT last_insert_rowid()").fetchone()[0]
                else:
                    word_id = word_id[0]
                
                conn.execute('''INSERT INTO word_frequencies (word_id, doc_id, Frequency) VALUES (?, ?, ?);''', (word_id, doc_id, i['word'][j]))
            
        
        conn.commit()
     
    def update_button_click(self):
        input_update = self.textEdit_Update.toPlainText()
        print(input_update)
        self.textBrowser_Console_Edit.clear()
        self.textBrowser_Console_Edit.append(input_update)
    
    def remove_button_click(self):
        input_remove = self.textEdit_Remove.toPlainText()
        print(input_remove)
        self.textBrowser_Console_Edit.clear()
        self.textBrowser_Console_Edit.append(input_remove)

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        #options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(MainWindow,"Openfile", "","database file (*.db);;sqlite file (*.sqlite3)", options=options)
        if fileName:
            self.file_name = fileName
            print(self.file_name)
        
            self.populate_table()
        '''   
         # Call method to populate table with data from database
        try:
            self.populate_table()
        except:
            # create a QMessageBox object
            alert = QMessageBox()
            
            # set the message box text and tyspe of alert
            alert.setText("database doesn't match!")
            alert.setIcon(QMessageBox.Warning)
            
            # display the alert box  
            alert.exec_()'''

    def populate_table(self):
        #print("DATABASE is conneted")
        #global db_dir
        #db_dir = self.file_name
        # Connect to database and execute SELECT statement
        conn = sqlite3.connect(db_dir)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM documents')
        #try:
            #cursor.execute('SELECT * FROM documents')
        #except:
            #print("It's is not my database")
        documents = cursor.fetchall()
        # Insert data into table
        
        self.table_showDatabase.setColumnCount(len(documents[0]))
        self.table_showDatabase.setRowCount(len(documents))

        for row in range(len(documents)):
            for col in range(len(documents[0])):
                item = QtWidgets.QTableWidgetItem(str(documents[row][col]))
                self.table_showDatabase.setItem(row, col, item)

        
        print("Database is showing")
        # Close database connection
        conn.close()
        
    def search_input(self):
        input_value = self.Search_input.toPlainText()
        print(input_value.lower())
        Result_search = []
        Result_search = self.sentence_search(input_value.lower())
        self.table_showDatabase.setColumnCount(0)
        self.table_showDatabase.setRowCount(0)
        try:
            self.table_showDatabase.setColumnCount(len(Result_search[0]))
            self.table_showDatabase.setRowCount(len(Result_search))
            for row in range(len(Result_search)):
                for col in range(len(Result_search[0])):
                    self.table_showDatabase.setItem(row, col, QtWidgets.QTableWidgetItem(str(Result_search[row][col])))
        except:
            error = "Not found"
            self.table_showDatabase.setColumnCount(1)
            self.table_showDatabase.setRowCount(1)
            for row in range(1):
                for col in range(1):
                    self.table_showDatabase.setItem(row, col, QtWidgets.QTableWidgetItem(str(error)))
            
           
            
    def sentence_search(self,search_term):
        
        conn = sqlite3.connect(db_dir)
        cursor = conn.cursor()

        # Split the query into individual words
        search_term = [search_term]
        clean_sentence = self.cleansing(search_term)
        words = self.spacy_process(clean_sentence)

        # Retrieve the documents that contain each word
        doc_lists = []
        for word in words:
            cursor.execute("SELECT Doc_ID, TF_IDF FROM word_frequencies JOIN words ON words.ID = word_frequencies.word_ID WHERE word = ?", (word,))
            doc_list = cursor.fetchall()
            doc_lists.append(doc_list)

        # Merge the document lists using the TF-IDF scores
        doc_scores = {}
        for doc_list in doc_lists:
            for doc_id, tf_idf in doc_list:
                if doc_id in doc_scores:
                    doc_scores[doc_id] += tf_idf
                else:
                    doc_scores[doc_id] = tf_idf

        # Rank the documents by their overall relevance
        ranked_docs = sorted(doc_scores.items(), key=lambda x: x[1], reverse=True)

        # Retrieve the links and titles of the top documents
        results = []
        for doc_id, score in ranked_docs:
            cursor.execute("SELECT Link, Title FROM documents WHERE ID = ?", (doc_id,))
            link, title = cursor.fetchone()
            results.append((link, title))

        conn.close()

        return results
        
    
    def spacy_process(self,text):
        
        nlp = spacy.load('en_core_web_sm')
        doc = nlp(text)
        
    #Tokenization and lemmatization 
        lemma_list = []
        for token in doc:
            lemma_list.append(token.lemma_)
        #print("Tokenize+Lemmatize:")
        #print(lemma_list)
        
        #Filter the stopword
        filtered_sentence =[] 
        for word in lemma_list:
            lexeme = nlp.vocab[word]
            if lexeme.is_stop == False:
                filtered_sentence.append(word) 
        
        #Remove punctuation
        punctuations="?:!.,;"
        for word in filtered_sentence:
            if word in punctuations:
                filtered_sentence.remove(word)
        #print(" ")
        #3print("Remove stopword & punctuation: ")
        #print(filtered_sentence)
        return filtered_sentence

    def cleansing(self,body):
        for i in body:
            output = i.replace('\n', '  ').replace('\xa0', '  ').replace('®', ' ').replace(';', ' ')
            output = " ".join(output.split())
        return output 

    def get_word(self,body):
        words = self.spacy_process(body)
        word_freq = {}
        for word in words:
            if word in word_freq:
                word_freq[word] += 1
            else:
                word_freq[word] = 1
        return word_freq
    
    def scrap_tags(self,url):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        try:
            title_tag = soup.find('title').text
        except:
            title_tag = soup.find('title')
        try:
            body_tag = soup.find('body')
            text_below_body = body_tag.get_text() 
        except:
            text_below_body ='Not Found'
        body_list =[]
        body_list.append(text_below_body)
        return (body_list,title_tag)
    
    def make_doc(self,link,ref):
        self.textBrowser.clear()
        newlink=link.replace(" ", "")
        d=dict()    
        body,word,title,location = self.check_lang(newlink)
        if body == None:
            body = 'None'
        self.textBrowser.append("Link : "+link)
        self.textBrowser.append("Title : "+title)
        self.textBrowser.append("Location : "+str(location))
        d['link']= link
        d['title'] = title
        d['body']=body
        d['location']=location
        d['word'] = word
        for i in ref:
            
            if link.startswith(i):
                d['ref'] = ref[i]
                
            else:
                d['ref'] = 0
        return d

    
    def get_ref(self):
        conn = sqlite3.connect(db_dir)
        domain = conn.execute("SELECT domain_link FROM domain_link ;").fetchall()
        domain = [t[0] for t in domain]
        for i in domain :
            web = spyder(domain,i,1)
            ref = web.get_check_ref()
        return ref
    
    def update_ref(self):
        conn = sqlite3.connect('../Week10/inverted_index2.db')
        domain = conn.execute("SELECT domain_link FROM domain_link ;").fetchall()
        domain = [t[0] for t in domain]
        for i in domain :
            web = spyder(domain,i,1)
            ref = web.get_check_ref()
        check_link = conn.execute("SELECT link FROM documents ;").fetchall()
        check_link = [t[0] for t in check_link]
        for j in check_link:
            for k in ref:
                if j.startswith(k):
                    conn.execute('UPDATE documents SET REF = ? WHERE link = ? ', (ref[k], j,))
        conn.commit()

    def eng_location(self,data,title):
        try:
            entities = locationtagger.find_locations(text = data[0])
            location = entities.countries
            if location == []:
                entities = locationtagger.find_locations(text = title)
                location = entities.countries
                if location ==[]:
                    location = ['None']
        except:
            location = ['None']
        return location 
    
    def check_lang(self,url:str):
        data_lang,title = self.scrap_tags(url)
        try:
            percent = pythainlp.util.countthai(data_lang[0][0])
            if percent >50:
                thai_nlp = self.Thai(data_lang[0]) 
                word = thai_nlp.word
                try:
                    location = 'จ.'+max(thai_nlp.get_location().keys())
                except:
                    location = 'Thailand'
                new_list = [s.strip().replace('"', '') for s in word if s.strip()]
                while '' in new_list:
                    new_list.remove('')
                word = self.get_word(new_list)
                return data_lang,word,title,location
            else:
                clean_body=self.cleansing(data_lang)
                body = self.cleansing(data_lang)
                word = self.get_word(body)
                location = self.eng_location(data_lang,title)
                return clean_body,word,title,location
        except:
            clean_body=self.cleansing(data_lang)
            body = self.cleansing(data_lang)
            word = self.get_word(body)
            location = self.eng_location(data_lang,title)
            return clean_body,word,title,location
        
    

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Search Engine"))
        self.label_Queue.setText(_translate("MainWindow", "Queue"))
        self.label_Depth.setText(_translate("MainWindow", "Depth"))
        self.save_path.setText(_translate("MainWindow", "Save as"))
        self.label_Input_domain.setText(_translate("MainWindow", "INPUT Domain links"))
        self.Button_OpenQueue.setText(_translate("MainWindow", "Open \n" " Database"))
        self.Button_PAUSE.setText(_translate("MainWindow", "PAUSE"))
        self.Button_RESUME.setText(_translate("MainWindow", "RESUME"))
        self.path_file.setText(_translate("MainWindow", "Save as : Please Select Save directory"))
        self.Button_Index.setText(_translate("MainWindow", "Index"))
        self.label_Total.setText(_translate("MainWindow", "TOTAL"))
        self.Button_ADD.setText(_translate("MainWindow", "ADD"))
        self.Button_EDIT.setText(_translate("MainWindow", "EDIT"))
        self.Button_REMOVE.setText(_translate("MainWindow", "REMOVE"))
        self.Button_CRAWLER.setText(_translate("MainWindow", "Crawler"))
        self.tabWidget_edit.setTabText(self.tabWidget_edit.indexOf(self.tab_scrapping), _translate("MainWindow", "scrap"))
        self.Button_view_path.setText(_translate("MainWindow", "SELECT DATABASE"))
        self.Search_button.setText(_translate("MainWindow", "Search"))
        self.label_data.setText(_translate("MainWindow", "DATA "))
        self.tabWidget_edit.setTabText(self.tabWidget_edit.indexOf(self.tab_Search), _translate("MainWindow", "Search"))
        self.Button_update.setText(_translate("MainWindow", "UPDATE"))
        self.Button_Remove.setText(_translate("MainWindow", "REMOVE"))
        self.label_Remove.setText(_translate("MainWindow", "REMOVE :"))
        self.label_UPDATE.setText(_translate("MainWindow", "UPDATE :"))
        self.tabWidget_edit.setTabText(self.tabWidget_edit.indexOf(self.tab_edit), _translate("MainWindow", "Edit"))
        self.label_Spatial.setText(_translate("MainWindow", "Spatial"))
        self.label_Topkeywords.setText(_translate("MainWindow", "Top keywords"))
        self.tabWidget_edit.setTabText(self.tabWidget_edit.indexOf(self.tab_Visualization), _translate("MainWindow", "Visualization"))

class SpiderThread(QThread):
    finished = pyqtSignal(list)
    progress_signal = pyqtSignal(str)
    count_links_signal = pyqtSignal(list)
    each_links_finished = pyqtSignal(int)
    #label_links_scraping = pyqtSignal(str)
    def __init__(self, target_links, depth_value):
        super().__init__()
        self.target_links = target_links
        self.depth_value = depth_value
        self.threads = []  # List to hold the threads for each link
        
    def run(self):
        domain_links = []
        for i in self.target_links:
            thread = LinkThread(i, self.depth_value, self.progress_signal, self.count_links_signal, self.each_links_finished)
            self.threads.append(thread)
            print(i)
            thread.start()
        
        # Wait for all threads to finish before emitting the finished signal
        for thread in self.threads:
            thread.wait()
            domain_links.extend(thread.result_crawler)
            
        self.finished.emit(domain_links)
        
        
class LinkThread(QThread):
    def __init__(self, link, depth, progress_signal, count_links_signal, each_links_finished):
        super().__init__()
        self.link = link
        self.depth = depth
        self.progress_signal = progress_signal
        self.count_links_signal = count_links_signal
        self.each_links_finished = each_links_finished
        self.result_crawler = []
        
    def run(self):
        
        web_spyder = spyder2([self.link], self.link, self.depth, self.progress_signal, self.count_links_signal)  # <-- pass progress_signal to spyder
        self.result_crawler = web_spyder.get_crawler()
        self.each_links_finished.emit(1)
        

class spyder2():
    def __init__(self, links, base_url, depth, progress_signal, count_links_signal):
        self.progress_signal = progress_signal
        self.count_links_signal = count_links_signal
        #self.each_links_finished = each_links_finished
        self.base_url = base_url
        target_links = {}
        for i in links:
            target_links[i] = 0
        self.target_links = target_links
        self.depth = depth
        self.total_links = 0
        self.crawled_links = 0
        #self.counter = 0 # initialize counter variable
        #self.lcd_Number = lcd_Number

    def crawl(self, url, n, depth, visited):
        if depth < n:
            visited.add(url)
            headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}
            time.sleep(0.3)
            response = requests.get(url, headers=headers)
            try:
                soup = BeautifulSoup(response.text, 'html.parser')
            except:
                soup = BeautifulSoup(response.text, 'lxml')
            links = soup.find_all('a')
            links = [link.get('href') for link in links if link.get('href') and not link.get('href').startswith('#')]
            links = [urljoin(url, link) for link in links if link]

            for link in links:
                if link not in visited:
                    link = link.replace(' ', '')
                    visited.add(link)
                    if link.startswith(url):
                        self.crawl(link, n=n, depth=depth+1, visited=visited)
                    self.progress_signal.emit(link)
                    self.crawled_links += 1
                    #self.counter += 1 # increment counter variable
                    self.count_links_signal.emit([self.crawled_links,url])
                    
                    #self.lcd_Number.display(self.counter) # update LCD number
        return visited

    def get_crawler(self):
        
        self.result_crawler = self.crawl(self.base_url, self.depth, 0, set())
        #self.counter += 1
        #self.count_signal.emit(self.counter)
        return self.result_crawler

    def get_check_domain(self):
        self.check_domain_result = self.check_domain(self.base_url, self.get_crawler())
        return self.check_domain_result

    def get_check_not_domain(self):
        self.check_not_domain_result = self.check_not_domain(self.base_url, self.get_crawler())
        return self.check_not_domain_result

    def get_check_ref(self):
        self.check_ref_result = self.check_ref(self.get_check_not_domain(), self.target_links)
        return self.check_ref_result

    def get_all(self):
        crawl = self.crawl(self.base_url, self.depth, 0, set())
        check_domain = self.check_domain(self.base_url, crawl)
        check_not_domain = self.check_not_domain(self.base_url, crawl)
        check_ref = self.check_ref(check_not_domain, self.target_links)
        return check_domain, check_ref

    
    def check_domain(self,base_url,links):
        result= set()
        for link in links :
            if link.startswith(base_url):
                result.add(link)
        return result
    
    def check_not_domain(self,base_url,links):
        result= set()
        for link in links :
            if not link.startswith(base_url):
                result.add(link)
        return result
    
    def check_ref(self,links,target_links):
        for i in links:
            for j in target_links:
                if i.startswith(j):
                    target_links[j]+=1
        return target_links

class spyder:
    def __init__( self ,links,base_url,depth ):
        self.base_url = base_url
        target_links={}
        for i in links:
            target_links[i]=0 
        self.target_links = target_links
        self.depth = depth
    
    def get_crawler(self):
        self.result_crawler = self.crawl(self.base_url,self.depth,0,set())
        return self.result_crawler
    
    def get_check_domain(self):
        self.check_domain_result = self.check_domain(self.base_url,self.get_crawler())
        return self.check_domain_result
    
    def get_check_not_domain(self):
        self.check_not_domain_result = self.check_not_domain(self.base_url,self.get_crawler())   
        return self.check_not_domain_result
    
    def get_check_ref(self):
        self.check_ref_result = self.check_ref(self.get_check_not_domain(),self.target_links)
        return self.check_ref_result
    
    def crawl(self,url,n, depth,visited):
        if depth < n :
            visited.add(url)
            headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}
            time.sleep(0.3)
            response = requests.get(url,headers=headers)
            try:
                soup = BeautifulSoup(response.text, 'html.parser')
            except:
                soup = BeautifulSoup(response.text, 'lxml')
            links = soup.find_all('a')
            links = [link.get('href') for link in links if link.get('href') and not link.get('href').startswith('#')]
            links = [urljoin(url, link) for link in links if link]

            for link in links:
                if link not in visited:
                    link = link.replace(' ','')
                    visited.add(link)
                    if link.startswith(url):
                        self.crawl(link,n=n,depth=depth+1, visited=visited)
        return visited
    
    def check_domain(self,base_url,links):
        result= set()
        for link in links :
            if link.startswith(base_url):
                result.add(link)
        return result
    
    def check_not_domain(self,base_url,links):
        result= set()
        for link in links :
            if not link.startswith(base_url):
                result.add(link)
        return result
    
    def check_ref(self,links,target_links):
        for i in links:
            for j in target_links:
                if i.startswith(j):
                    target_links[j]+=1
        return target_links
    
class Thai:
    def __init__(self,data:list):
        self.data_value = data
        self.sentence = self.get_sentence()
        self.summarize = self.get_summarize()
        self.word = self.get_word() 
    def make_sentence(self,list_word):
        list_word = [list_word]
        self.sentence_value = ''
        for i in list_word:
            for i in list_word:
                if pythainlp.util.countthai(i)<10:
                    list_word.remove(i)
        self.sentence_value = ' '.join(list_word)
        return self.sentence_value
    def get_sentence(self):
        self.sentence_result = self.make_sentence(self.data_value)
        return self.sentence_result
    def get_word(self):
        self.word_value = tokenizer(self.sentence, engine="newmm")
        return self.word_value
    def get_summarize(self):
        self.summarize_result =[]
        self.summarize_result = summarize(self.sentence,n=5)
        return self.summarize_result
    def location(self):
        self.data = self.get_tokenize()
        self.location_value = tag_provinces(self.data)
        self.Result_location = [entry for entry in self.location_value if entry[1] == 'B-LOCATION']
        return self.Result_location
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())