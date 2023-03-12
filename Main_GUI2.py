import requests
from bs4 import BeautifulSoup
import time
from urllib.parse import urljoin

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QInputDialog, QLineEdit, QListWidgetItem, QMessageBox



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1044, 878)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setMinimumSize(QtCore.QSize(640, 480))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_scrapping = QtWidgets.QWidget()
        self.tab_scrapping.setMouseTracking(False)
        self.tab_scrapping.setAccessibleName("")
        self.tab_scrapping.setAutoFillBackground(False)
        self.tab_scrapping.setObjectName("tab_scrapping")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_scrapping)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_Total = QtWidgets.QLabel(self.tab_scrapping)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_Total.setFont(font)
        self.label_Total.setObjectName("label_Total")
        self.verticalLayout_3.addWidget(self.label_Total)
        self.gridLayout_2.addLayout(self.verticalLayout_3, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.spinBox_Depth = QtWidgets.QSpinBox(self.tab_scrapping)
        self.spinBox_Depth.setMinimum(1)
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
        self.spinBox_Depth.setObjectName("spinBox_Depth")
        self.horizontalLayout.addWidget(self.spinBox_Depth)
        self.label_Depth = QtWidgets.QLabel(self.tab_scrapping)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_Depth.setFont(font)
        self.label_Depth.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_Depth.setObjectName("label_Depth")
        self.horizontalLayout.addWidget(self.label_Depth)
        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 1, 1, 1)
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
        self.listWidget.setStyleSheet('font-size: 20px;')
        self.load_input_domain()

        self.verticalLayout_2.addWidget(self.listWidget)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.textBrowser = QtWidgets.QTextBrowser(self.tab_scrapping)

        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setStyleSheet('font-size: 18px;')
        self.textBrowser.setAcceptRichText(True)
        self.textBrowser.setOpenExternalLinks(True)

        self.verticalLayout_4.addWidget(self.textBrowser)
        self.progressBar = QtWidgets.QProgressBar(self.tab_scrapping)
        self.progressBar.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.progressBar.setProperty("value", 50)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_4.addWidget(self.progressBar)
        self.gridLayout_2.addLayout(self.verticalLayout_4, 2, 0, 1, 3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, 50, -1, -1)
        self.verticalLayout.setSpacing(30)
        self.verticalLayout.setObjectName("verticalLayout")
        self.button_ADD = QtWidgets.QPushButton(self.tab_scrapping)

        self.button_ADD.setObjectName("button_ADD")
        self.button_ADD.clicked.connect(self.Addlinks)
        self.verticalLayout.addWidget(self.button_ADD)

        self.Button_EDIT = QtWidgets.QPushButton(self.tab_scrapping)
        self.Button_EDIT.setObjectName("Button_EDIT")
        self.Button_EDIT.clicked.connect(self.editlinks)
        self.verticalLayout.addWidget(self.Button_EDIT)
        self.Button_REMOVE = QtWidgets.QPushButton(self.tab_scrapping)
        self.Button_REMOVE.setObjectName("Button_REMOVE")
        self.Button_REMOVE.clicked.connect(self.removelink)
        self.verticalLayout.addWidget(self.Button_REMOVE)
        self.Button_Start = QtWidgets.QPushButton(self.tab_scrapping)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Button_Start.setFont(font)
        self.Button_Start.setIconSize(QtCore.QSize(16, 16))
        self.Button_Start.setAutoDefault(False)
        self.Button_Start.setDefault(False)
        self.Button_Start.setFlat(False)
        self.Button_Start.setObjectName("Button_Start")
        self.Button_Start.clicked.connect(self.clicked_start)

        self.verticalLayout.addWidget(self.Button_Start)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 2, 2, 1)
        self.tabWidget.addTab(self.tab_scrapping, "")
        self.tab_view = QtWidgets.QWidget()
        self.tab_view.setObjectName("tab_view")
        self.tabWidget.addTab(self.tab_view, "")
        self.tab_Visualization = QtWidgets.QWidget()
        self.tab_Visualization.setObjectName("tab_Visualization")
        self.tabWidget.addTab(self.tab_Visualization, "")
        self.tab_Search = QtWidgets.QWidget()
        self.tab_Search.setObjectName("tab_Search")
        self.tabWidget.addTab(self.tab_Search, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

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
            text, ok = QInputDialog.getText(MainWindow,"Edit Student","Student Name",QLineEdit.Normal,item.text())
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
        Domain_list = []
        for i in range(self.listWidget.count()):
            item = self.listWidget.item(i)
            Domain_list.append(item.text())
        depth_value = self.spinBox_Depth.value()
        '''
        print("Links = "+str(Domain_list))
        
        #print("depth = "+str(depth_value))
        for i in Domain_list:
            value = self.crawl(i,depth_value,0,set())
            
            print(value)'''
        
        for i in Domain_list:
            web_spyder=spyder(Domain_list,i,depth_value)
            domain_links,target_links =web_spyder.get_all()
            for i in domain_links:
                self.textBrowser.append(i)
        self.label_Total.setObjectName("label_Total : "+ str(len(domain_links)))
        


        

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
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_scrapping), _translate("MainWindow", "scrap"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_view), _translate("MainWindow", "view"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Visualization), _translate("MainWindow", "Visualization"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Search), _translate("MainWindow", "Search"))

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
    
    def get_all(self):
        crawl = self.crawl(self.base_url,self.depth,0,set())
        check_domain =  self.check_domain(self.base_url,crawl) 
        check_not_domain = self.check_not_domain(self.base_url,crawl)
        check_ref = self.check_ref(check_not_domain,self.target_links)
        return check_domain,check_ref
    
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
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
