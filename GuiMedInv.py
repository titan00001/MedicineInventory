from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MedInv(object):
    
    def setupUi(self, MainWindow):
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 791, 581))
        self.tabWidget.setObjectName("tabWidget")
        
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        
        self.label_Title = QtWidgets.QLabel(self.tab)
        self.label_Title.setGeometry(QtCore.QRect(240, 0, 221, 31))
        self.label_Title.setObjectName("label_Title")
        
        self.line = QtWidgets.QFrame(self.tab)
        self.line.setGeometry(QtCore.QRect(550, 20, 16, 481))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        
        
        self.pushButton_SaveScienInfo = QtWidgets.QPushButton(self.tab)
        self.pushButton_SaveScienInfo.setGeometry(QtCore.QRect(420, 500, 101, 23))
        self.pushButton_SaveScienInfo.setObjectName("pushButton_SaveScienInfo")
        
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(420, 230, 91, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        
        self.pushButton_clearInfo = QtWidgets.QPushButton(self.tab)
        self.pushButton_clearInfo.setGeometry(QtCore.QRect(200, 500, 91, 23))
        
        
        self.line_2 = QtWidgets.QFrame(self.tab)
        self.line_2.setGeometry(QtCore.QRect(0, 260, 541, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        
        self.label_TitleComInfo = QtWidgets.QLabel(self.tab)
        self.label_TitleComInfo.setGeometry(QtCore.QRect(30, 30, 151, 31))
        self.label_TitleComInfo.setObjectName("label_TitleComInfo")
        
        self.label_5_TitleScienInfo = QtWidgets.QLabel(self.tab)
        self.label_5_TitleScienInfo.setGeometry(QtCore.QRect(20, 290, 161, 31))
        self.label_5_TitleScienInfo.setObjectName("label_5_TitleScienInfo")
        
        self.label_commNameInScienInfo = QtWidgets.QLabel(self.tab)
        self.label_commNameInScienInfo.setGeometry(170,290,161,31)
        
        
        
        
        self.label_6_CommName = QtWidgets.QLabel(self.tab)
        self.label_6_CommName.setGeometry(QtCore.QRect(30, 90, 91, 21))
        self.label_6_CommName.setObjectName("label_6_CommName")
        
        self.label_8_MfgDate = QtWidgets.QLabel(self.tab)
        self.label_8_MfgDate.setGeometry(QtCore.QRect(30, 140, 81, 21))
        self.label_8_MfgDate.setObjectName("label_8_MfgDate")
        
        self.label_9_Price = QtWidgets.QLabel(self.tab)
        self.label_9_Price.setGeometry(QtCore.QRect(30, 190, 91, 21))
        self.label_9_Price.setObjectName("label_9_Price")
        
        self.label_10_GenName = QtWidgets.QLabel(self.tab)
        self.label_10_GenName.setGeometry(QtCore.QRect(20, 340, 91, 21))
        self.label_10_GenName.setObjectName("label_10_GenName")
        
        self.label_11_ExpTerm = QtWidgets.QLabel(self.tab)
        self.label_11_ExpTerm.setGeometry(QtCore.QRect(20, 390, 71, 21))
        self.label_11_ExpTerm.setObjectName("label_11_ExpTerm")
        
        self.label_12_Qty = QtWidgets.QLabel(self.tab)
        self.label_12_Qty.setGeometry(QtCore.QRect(20, 440, 71, 21))
        self.label_12_Qty.setObjectName("label_12_Qty")
       
        self.lineEdit_CommName = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_CommName.setGeometry(QtCore.QRect(170, 90, 181, 20))
        self.lineEdit_CommName.setObjectName("lineEdit_CommName")

        self.lineEdit_Price = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_Price.setGeometry(QtCore.QRect(170, 190, 181, 20))
        self.lineEdit_Price.setObjectName("lineEdit_Price")
        
        self.lineEdit_GenName = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_GenName.setGeometry(QtCore.QRect(170, 340, 181, 20))
        self.lineEdit_GenName.setObjectName("lineEdit_GenName")
        
        self.lineEdit_Qty = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_Qty.setGeometry(QtCore.QRect(170, 440, 181, 20))
        self.lineEdit_Qty.setObjectName("lineEdit_Qty")
        
        
        self.comboBox_ExpDateMonth_ExpDateYear = QtWidgets.QComboBox(self.tab)
        self.comboBox_ExpDateMonth_ExpDateYear.setGeometry(QtCore.QRect(170, 390, 81, 22))
        self.comboBox_ExpDateMonth_ExpDateYear.setObjectName("comboBox_ExpDateMonth_ExpDateYear")
        
        self.comboBox_2 = QtWidgets.QComboBox(self.tab)
        self.comboBox_2.setGeometry(QtCore.QRect(260, 390, 91, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        
        self.comboBox_mfg_month = QtWidgets.QComboBox(self.tab)
        self.comboBox_mfg_month.setGeometry(QtCore.QRect(170,140,81,22))
        
        self.comboBox_mfg_year = QtWidgets.QComboBox(self.tab)
        self.comboBox_mfg_year.setGeometry(QtCore.QRect(260,140,91,22))
        
        
        
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        
        self.pushButton_Confirm = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_Confirm.setGeometry(QtCore.QRect(330, 500, 100, 23))
        self.pushButton_Confirm.setObjectName("pushButton_Confirm")
        
        self.pushButton_addRow = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_addRow.setGeometry(QtCore.QRect(80, 500, 80, 23))
        
        self.pushButton_Refresh = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_Refresh.setGeometry(QtCore.QRect(200, 500, 80, 23))
        
        self.pushButton_NewBill = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_NewBill.setGeometry(QtCore.QRect(500, 500, 80, 23))
        
        self.Name = QtWidgets.QLineEdit(self.tab_2)
        self.Name.setGeometry(QtCore.QRect(100, 60, 271, 20))
        self.Name.setObjectName("Name")
        
        self.Doctor = QtWidgets.QLineEdit(self.tab_2)
        self.Doctor.setGeometry(QtCore.QRect(100, 109, 271, 21))
        self.Doctor.setObjectName("Doctor")
        
        self.Phone = QtWidgets.QLineEdit(self.tab_2)
        self.Phone.setGeometry(QtCore.QRect(100, 160, 271, 21))
        self.Phone.setObjectName("Phone")
        
        self.label_Name = QtWidgets.QLabel(self.tab_2)
        self.label_Name.setGeometry(QtCore.QRect(10, 60, 81, 21))
        self.label_Name.setObjectName("label_Name")
        
        self.label_2_DOC = QtWidgets.QLabel(self.tab_2)
        self.label_2_DOC.setGeometry(QtCore.QRect(10, 110, 81, 21))
        self.label_2_DOC.setObjectName("label_2_DOC")
        
        self.label_3_phone = QtWidgets.QLabel(self.tab_2)
        self.label_3_phone.setGeometry(QtCore.QRect(10, 160, 81, 21))
        self.label_3_phone.setObjectName("label_3_phone")
        
        self.label_4_date = QtWidgets.QLabel(self.tab_2)
        self.label_4_date.setGeometry(QtCore.QRect(400, 50, 121, 21))
        self.label_4_date.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4_date.setObjectName("label_4_date")
        
        
        
        self.search = QtWidgets.QLineEdit(self.tab_2)
        self.search.setGeometry(QtCore.QRect(590, 0, 191, 31))
        self.search.setInputMask("")
        self.search.setObjectName("search")
        
        
        
        self.tableWidget = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget.setGeometry(QtCore.QRect(0, 230, 571, 251))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        
        self.listView_EditStock = QtWidgets.QListWidget(self.tab)
        self.listView_EditStock.setGeometry(QtCore.QRect(565, 20, 211, 511))
        self.listView_EditStock.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.listView_EditStock.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.listView_EditStock.setObjectName("listView_EditStock")
        
        self.listView = QtWidgets.QListWidget(self.tab_2)
        self.listView.setGeometry(QtCore.QRect(590, 40, 191, 441))
        self.listView_EditStock.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.listView_EditStock.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.listView.setObjectName("listView")
        
        
        
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(40, 10, 381, 31))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.tabWidget.addTab(self.tab_2, "")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Medicine Inventory Manager"))
        self.label_Title.setText(_translate("MainWindow", "medicine inventory information"))
        self.pushButton_SaveScienInfo.setText(_translate("MainWindow", "Save"))
        self.label_TitleComInfo.setText(_translate("MainWindow", "Commercial Information"))
        self.label_5_TitleScienInfo.setText(_translate("MainWindow", "Scientific info"))
        self.pushButton_2.setText(_translate("MainWindow", "Save"))
        self.label_6_CommName.setText(_translate("MainWindow", "Commercial Name"))
        self.label_8_MfgDate.setText(_translate("MainWindow", "Mfg Date"))
        self.label_9_Price.setText(_translate("MainWindow", "Price"))
        self.label_10_GenName.setText(_translate("MainWindow", "Generic Name"))
        self.label_11_ExpTerm.setText(_translate("MainWindow", "Expiry tenure"))
        self.label_12_Qty.setText(_translate("MainWindow", "Quantity"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Stock"))
        self.pushButton_Confirm.setText(_translate("MainWindow", "Confirm"))
        self.pushButton_addRow.setText(_translate("MainWindow", "Add Row"))
        self.pushButton_Refresh.setText(_translate("MainWindow", "Refresh Data"))
        self.pushButton_NewBill.setText(_translate("MainWindow", "New Bill"))
        self.pushButton_clearInfo.setText(_translate("MainWindow", "Clear"))
        self.label_Name.setText(_translate("MainWindow", "Name"))
        self.label_2_DOC.setText(_translate("MainWindow", "Doctor"))
        self.label_3_phone.setText(_translate("MainWindow", "Phone"))
        self.label_4_date.setText(_translate("MainWindow", "Date"))
        self.search.setText(_translate("MainWindow", "Search by name"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Item"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Quantity"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Rate"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Tax Rate"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Price"))
        self.label_2.setText(_translate("MainWindow", "Bill Information"))
        self.label_commNameInScienInfo.setText(_translate("MainWindow", "Common Name"))
        
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Customer"))

