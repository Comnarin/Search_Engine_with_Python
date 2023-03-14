import requests
from bs4 import BeautifulSoup
import time
from urllib.parse import urljoin

import spacy
from spacy.tokenizer import Tokenizer
from spacy.lang.en import English

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QInputDialog, QLineEdit, QListWidgetItem, QMessageBox,QFileDialog,QHeaderView
from PyQt5.QtCore import QThread, pyqtSignal

from PyQt5 import QtCore, QtGui, QtWidgets
import math
import sqlite3


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 876)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
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
        self.label_Depth = QtWidgets.QLabel(self.tab_scrapping)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_Depth.setFont(font)
        self.label_Depth.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_Depth.setObjectName("label_Depth")
        self.horizontalLayout_2.addWidget(self.label_Depth)
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
        self.horizontalLayout_2.addWidget(self.spinBox_Depth)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_Input_domain = QtWidgets.QLabel(self.tab_scrapping)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_Input_domain.setFont(font)
        self.label_Input_domain.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_Input_domain.setObjectName("label_Input_domain")
        self.verticalLayout_2.addWidget(self.label_Input_domain)
        self.listWidget = QtWidgets.QListWidget(self.tab_scrapping)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_2.addWidget(self.listWidget)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, 50, -1, -1)
        self.verticalLayout.setSpacing(30)
        self.verticalLayout.setObjectName("verticalLayout")
        self.button_ADD = QtWidgets.QPushButton(self.tab_scrapping)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.button_ADD.setFont(font)
        self.button_ADD.setObjectName("button_ADD")
        self.verticalLayout.addWidget(self.button_ADD)
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
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.Button_Start = QtWidgets.QPushButton(self.tab_scrapping)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Button_Start.setFont(font)
        self.Button_Start.setIconSize(QtCore.QSize(16, 16))
        self.Button_Start.setAutoDefault(False)
        self.Button_Start.setDefault(False)
        self.Button_Start.setFlat(False)
        self.Button_Start.setObjectName("Button_Start")
        self.verticalLayout.addWidget(self.Button_Start)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 2, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.textBrowser = QtWidgets.QTextBrowser(self.tab_scrapping)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_4.addWidget(self.textBrowser)
        self.progressBar = QtWidgets.QProgressBar(self.tab_scrapping)
        self.progressBar.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_4.addWidget(self.progressBar)
        self.gridLayout_2.addLayout(self.verticalLayout_4, 4, 0, 1, 1)
        self.tabWidget_edit.addTab(self.tab_scrapping, "")
        self.tab_view = QtWidgets.QWidget()
        self.tab_view.setObjectName("tab_view")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_view)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Button_openfile = QtWidgets.QPushButton(self.tab_view)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Button_openfile.setFont(font)
        self.Button_openfile.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Button_openfile.setObjectName("Button_openfile")
        self.Button_openfile.clicked.connect(self.openFileNameDialog)
        self.verticalLayout_3.addWidget(self.Button_openfile)
        self.label_data_view = QtWidgets.QLabel(self.tab_view)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_data_view.setFont(font)
        self.label_data_view.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_data_view.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_data_view.setObjectName("label_data_view")
        self.verticalLayout_3.addWidget(self.label_data_view)
        self.splitter = QtWidgets.QSplitter(self.tab_view)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.textEdit_2 = QtWidgets.QTextEdit(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setObjectName("textEdit_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.search_input)
        self.verticalLayout_3.addWidget(self.splitter)
        self.table_view = QtWidgets.QTableWidget(self.tab_view)
        self.table_view.setObjectName("table_view")
        self.table_view.setColumnCount(0)
        self.table_view.setRowCount(0)
        self.table_view.horizontalHeader().setVisible(True)
        self.verticalLayout_3.addWidget(self.table_view)
        self.tabWidget_edit.addTab(self.tab_view, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout = QtWidgets.QGridLayout(self.tab)
        self.gridLayout.setObjectName("gridLayout")
        self.textEdit_3 = QtWidgets.QTextEdit(self.tab)
        self.textEdit_3.setObjectName("textEdit_3")
        self.gridLayout.addWidget(self.textEdit_3, 1, 2, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.tab)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 1, 3, 1, 1)
        self.progressBar_2 = QtWidgets.QProgressBar(self.tab)
        self.progressBar_2.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Kenya))
        self.progressBar_2.setProperty("value", 24)
        self.progressBar_2.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar_2.setObjectName("progressBar_2")
        self.gridLayout.addWidget(self.progressBar_2, 2, 2, 1, 1)
        self.textEdit_4 = QtWidgets.QTextEdit(self.tab)
        self.textEdit_4.setObjectName("textEdit_4")
        self.gridLayout.addWidget(self.textEdit_4, 4, 1, 1, 2)
        self.pushButton_4 = QtWidgets.QPushButton(self.tab)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 4, 3, 1, 1)
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.gridLayout.addWidget(self.textBrowser_2, 6, 0, 1, 3)
        self.progressBar_3 = QtWidgets.QProgressBar(self.tab)
        self.progressBar_3.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.progressBar_3.setProperty("value", 24)
        self.progressBar_3.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar_3.setObjectName("progressBar_3")
        self.gridLayout.addWidget(self.progressBar_3, 5, 1, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        self.tabWidget_edit.addTab(self.tab, "")
        self.tab_Visualization = QtWidgets.QWidget()
        self.tab_Visualization.setObjectName("tab_Visualization")
        self.tabWidget_edit.addTab(self.tab_Visualization, "")
        self.tab_Search = QtWidgets.QWidget()
        self.tab_Search.setObjectName("tab_Search")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_Search)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label = QtWidgets.QLabel(self.tab_Search)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.tab_Search)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_3.addWidget(self.pushButton, 3, 1, 1, 1)
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.tab_Search)
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.gridLayout_3.addWidget(self.textBrowser_3, 4, 0, 1, 3)
        self.textEdit = QtWidgets.QTextEdit(self.tab_Search)
        self.textEdit.setMinimumSize(QtCore.QSize(0, 0))
        self.textEdit.setBaseSize(QtCore.QSize(0, 0))
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_3.addWidget(self.textEdit, 1, 1, 2, 1)
        self.tabWidget_edit.addTab(self.tab_Search, "")
        self.gridLayout_4.addWidget(self.tabWidget_edit, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget_edit.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def openFileNameDialog(self):
        options = QFileDialog.Options()
        #options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(MainWindow,"Openfile", "","sqlite file (*.sqlite3);;database file (*.db)", options=options)
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
        print("DATABASE is conneted")
        global db_dir
        db_dir = (self.file_name)
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
        
        self.table_view.setColumnCount(len(documents[0]))
        self.table_view.setRowCount(len(documents))

        for row in range(len(documents)):
            for col in range(len(documents[0])):
                item = QtWidgets.QTableWidgetItem(str(documents[row][col]))
                self.table_view.setItem(row, col, item)

        
        print("Database is showing")
        # Close database connection
        conn.close()
        
    def search_input(self):
        input_value = self.textEdit_2.toPlainText()
        print(input_value)
        Result_search = []
        Result_search = self.sentence_search(input_value)
        try:
            self.table_view.setColumnCount(len(Result_search[0]))
            self.table_view.setRowCount(len(Result_search))
            for row in range(len(Result_search)):
                for col in range(len(Result_search[0])):
                    self.table_view.setItem(row, col, QtWidgets.QTableWidgetItem(str(Result_search[row][col])))
        except:
            error = "Not found"
            self.table_view.setColumnCount(2)
            self.table_view.setRowCount(2)
            for row in range(2):
                for col in range(2):
                    self.table_view.setItem(row, col, QtWidgets.QTableWidgetItem(str(error)))
            
           
            
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
    
    def scrape_tags(self,url):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        try:
            title_tag = soup.find('title').text
        except:
            title_tag = soup.find('title')
        body_tag = soup.find('body')
        text_below_body = body_tag.get_text() 
        body_list =[]
        body_list.append(text_below_body)
        return (body_list,title_tag)
    
    def make_doc(self,link,target_links):
        #print(link)
        link.replace(" ", "")
        d=dict()
        #self.textBrowser.clear()
        body, title = self.scrape_tags(link)
        body=self.cleansing(body)
        word = self.get_word(body)
        #self.textBrowser.append(str(body))
        #self.textBrowser.append(str(word))

        d['link']= link
        d['title'] = title
        d['body']=body
        d['location']='location'
        d['word'] = word
        
        
        for k in target_links:
            if link.startswith(k):
                d['ref'] = target_links[k]
        #print(d)
        return d

    
    def get_doc(self,target_links,n):
        doc=[]
        num=0
        for i in target_links:
            print(target_links,i,n)
            web_spyder=spyder(target_links,i,n)
            domain_links,target_links =web_spyder.get_all()
            print('all link =', len(domain_links))
            for j in domain_links:
                num+=1
                d = self.make_doc(j,target_links)
                doc.append(d)
                #self.lcdNumber.display(num)
                print(num)
        return doc 

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Search Engine"))
        self.label_Total.setText(_translate("MainWindow", "TOTAL"))
        self.label_Depth.setText(_translate("MainWindow", "Depth"))
        self.label_Input_domain.setText(_translate("MainWindow", "INPUT Domain links"))
        self.button_ADD.setText(_translate("MainWindow", "ADD"))
        self.Button_EDIT.setText(_translate("MainWindow", "EDIT"))
        self.Button_REMOVE.setText(_translate("MainWindow", "REMOVE"))
        self.Button_Start.setText(_translate("MainWindow", "Start "))
        self.tabWidget_edit.setTabText(self.tabWidget_edit.indexOf(self.tab_scrapping), _translate("MainWindow", "scrap"))
        self.Button_openfile.setText(_translate("MainWindow", "OpenFile"))
        self.label_data_view.setText(_translate("MainWindow", "DATA "))
        self.pushButton_2.setText(_translate("MainWindow", "Search"))
        self.tabWidget_edit.setTabText(self.tabWidget_edit.indexOf(self.tab_view), _translate("MainWindow", "view"))
        self.pushButton_3.setText(_translate("MainWindow", "UPDATE"))
        self.pushButton_4.setText(_translate("MainWindow", "REMOVE"))
        self.label_3.setText(_translate("MainWindow", "REMOVE"))
        self.label_2.setText(_translate("MainWindow", "UPDATE"))
        self.tabWidget_edit.setTabText(self.tabWidget_edit.indexOf(self.tab), _translate("MainWindow", "Edit"))
        self.tabWidget_edit.setTabText(self.tabWidget_edit.indexOf(self.tab_Visualization), _translate("MainWindow", "Visualization"))
        self.label.setText(_translate("MainWindow", "Search"))
        self.pushButton.setText(_translate("MainWindow", "Search"))
        self.tabWidget_edit.setTabText(self.tabWidget_edit.indexOf(self.tab_Search), _translate("MainWindow", "Search"))

class spyder():
    def __init__(self, links, base_url, depth, progress_signal):
        self.progress_signal = progress_signal # store progress signal
        self.base_url = base_url
        target_links = {}
        for i in links:
            target_links[i] = 0
        self.target_links = target_links
        self.depth = depth

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
                    self.progress_signal.emit(link) # emit progress signal here
        return visited

    def get_crawler(self):
        self.result_crawler = self.crawl(self.base_url, self.depth, 0, set())
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
    
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
