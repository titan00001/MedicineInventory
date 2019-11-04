from PyQt5 import Qt,QtWidgets
from MedicineInventory.GuiMedInv import Ui_MedInv
from PyQt5.QtWidgets import QMainWindow, QListWidgetItem, QCompleter, QTableWidgetItem
from MedicineInventory.DBMedInv import MDdatabase
import datetime
import math

'''TO DO LIST:

    1.    Total in bill
    2.    Implement the search and completer function
    3.    Add quantity field in listWidget of bill
    4.    Handle empty input in bill : a bill must have name, doctor and phone number
    5.    Raise prompt if cell value is getting unknown data type
    6.    Add row on pressing enter
    7.    Reflect the date info for editing the medicine info on combo box
    8.    Raise prompt if same item is input in bill
    9.    Clear the info form stock widgets after saving info of bill
    10.   Raise prompt if line is empty
    11.   Add the relevant dialog box for better user experience
    
NOTE: LIST NOT SORTED ON BASIS OF PRIORITY'''

class MedManager(QMainWindow,Ui_MedInv):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        
        global d
        d = MDdatabase()
        
        self.DispTime()
        self.showMedicineList()
        self.initComboBox()
        
        self.pushButton_2.clicked.connect(self.setCommInfo)
        self.pushButton_SaveScienInfo.clicked.connect(self.setScienInfo)
        self.pushButton_Confirm.clicked.connect(self.custBillInfo)
        self.pushButton_addRow.clicked.connect(self.addRowInBill)
        self.pushButton_Refresh.clicked.connect(self.refreshData)
        self.pushButton_NewBill.clicked.connect(self.newBill)
        
        self.listView_EditStock.itemClicked.connect(self.editStock)
        self.listView.itemClicked.connect(self.addToBill)
    
        self.tableWidget.itemDoubleClicked.connect(self.clearBillRow)
        
    
    def refreshData(self):
        
        '''reflect the changes in tableWidget if cell value is modified'''
        
        row = self.tableWidget.rowCount() 
        for i in range(row):
            qty = int(self.tableWidget.item(i,1).text())
            rate = int(self.tableWidget.item(i,2).text())
            taxRate = int(self.tableWidget.item(i,3).text())
            price = math.ceil(qty*rate*(1+taxRate/100))
            self.tableWidget.setItem(i,4,QTableWidgetItem(str(price)))
            
    def newBill(self):
        
        '''clear all the received information in bill'''
        
        self.tableWidget.setRowCount(1)
        self.Name.clear()
        self.Doctor.clear()
        self.Phone.clear()
        
    
    def clearBillRow(self, item):
        '''delete the row if double clicked event is detected'''
        row = item.row()
        self.tableWidget.removeRow(row)
    
    
    def addToBill(self, item):
        '''add the information of selected item in tableWidget of bill'''
        name = str(item.text())
        info = d.getCommercialInfo(name)
        commonName = info[0]
        rate = info[2]
        taxRate = 12
        qty = 2
        price = math.ceil(int(rate)*qty*(1+(taxRate/100)))
        
        currentRow = self.tableWidget.rowCount() - 1
        
        self.tableWidget.setItem(currentRow,1,QTableWidgetItem(str(qty)))
        self.tableWidget.setItem(currentRow,0,QTableWidgetItem(str(commonName)))
        self.tableWidget.setItem(currentRow,2,QTableWidgetItem(str(rate)))
        self.tableWidget.setItem(currentRow,3,QTableWidgetItem(str(taxRate)))
        self.tableWidget.setItem(currentRow,4,QTableWidgetItem(str(price)))
        
        
            
    def addRowInBill(self):
        '''insert a new row in tableWidget of bill on detecting click of pushButton_addRow
        AND SETTING LAST ROW AS CURRENT ROW'''
        lastRow = self.tableWidget.rowCount() + 1
        self.tableWidget.setRowCount(lastRow)
        
        
        
    def editStock(self, item):
        '''edit the stock information of selected item'''
        name = str(item.text())
        info = d.getCommercialInfo(name)
        
        mfg_date = info[1]
        price = info[2]
        
        scienInfo = d.getScientificInfo(name)
        gen = scienInfo[1]
        exp_date = scienInfo[2]
        qty = scienInfo[3]
         
        self.getCommInfo(name,mfg_date,price)
        self.getScienInfo(name, gen, exp_date, qty)
        
    def getCommInfo(self,commonName,mfg_date,price):
        '''show the commercial info of medicine from database on widget'''
        '''not reflecting the value in combo box'''
        self.lineEdit_CommName.setText(str(commonName))
        self.lineEdit_Price.setText(str(price))
        mth,yr = mfg_date.split('-')
        self.comboBox_ExpDateMonth_ExpDateYear.setEditText(str(mth))
        self.comboBox_2.setEditText(str(yr))
        
    def getScienInfo(self,commonName,generic,exp_date,qty):
        '''show the scientific info of medicine from database on widget'''
        '''not reflecting the value in combo box'''
        self.label_commNameInScienInfo.setText(str(commonName))
        self.lineEdit_GenName.setText(str(generic))
        self.lineEdit_Qty.setText(str(qty))
        mth,yr = exp_date.split('-')
        
    
        
    def setCommInfo(self):
        '''returns the commercial information of medicine from user to database;
        change the label name in scientific field;
        recreates medicine list for both listWidget'''
        n = self.lineEdit_CommName.text()
        mfg_month = self.comboBox_mfg_month.currentText()
        mfg_year = self.comboBox_mfg_year.currentText()
        p = self.lineEdit_Price.text()
        dt = str(mfg_month) + '-' + str(mfg_year)
        
        d.inputCommInfo(n,dt,p)
        self.label_commNameInScienInfo.setText(n)
        self.showMedicineList()
        
        
    def setScienInfo(self):
        '''returns the scientific information of medicine from user to database'''
        n1 = self.label_commNameInScienInfo.text()
        n = self.lineEdit_GenName.text()
        exp_month = self.comboBox_ExpDateMonth_ExpDateYear.currentIndex()
        exp_year = self.comboBox_2.currentIndex()
        exp_date = str(exp_month)+'-'+str(exp_year)
        qty = self.lineEdit_Qty.text()
        d.inputScienInfo(n1,n,exp_date,qty)
        
        
        
    def custBillInfo(self):
        '''returns the customer information of medicine from user to database;
        activated on clicking confirm button on bill'''
        name = self.Name.text()
        doc_name = self.Doctor.text()
        phone = self.Phone.text()
        d.inputCustInfo(name,doc_name,phone)
        self.refreshData()
        
    def DispTime(self):
        '''display date and time in bill'''
        curr_time = datetime.datetime.now()
        curr_time_str = curr_time.strftime("%d, %b, %Y (%a)")
        self.label_4_date.setText(curr_time_str) 
        
        
    def showMedicineList(self):
        '''fetches all medicine name from database to listWidget'''
        stockList = self.listView_EditStock
        customerStockList = self.listView
        
        stockList.clear()
        customerStockList.clear()
        
        commercialNameList = d.getCommercialNameList()
        
        for medicine in commercialNameList:
            
            item  = QListWidgetItem()
            item.setText(medicine)
            customerStockList.addItem(item)
            
            
        for medicine in commercialNameList:
            
            item  = QListWidgetItem()
            item.setText(medicine)
            stockList.addItem(item)
            
            
            
    def searchItem(self):
        '''implements qCompleter from database; prints result not found in obvious case'''
        '''Not completed'''
        completer = 0
        searchList = QCompleter()
        searchList.setCaseSensitivity()
        searchList.setCompleter(completer)
            
    def initComboBox(self):
        
        '''Initialise the combo boxes with month name and year'''
        
        Monthlist = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
        YearList = [str(i) for i in range(1990,2030)]
        
        self.comboBox_ExpDateMonth_ExpDateYear.addItems(Monthlist)
        self.comboBox_2.addItems(YearList)
        self.comboBox_mfg_month.addItems(Monthlist)
        self.comboBox_mfg_year.addItems(YearList)
        
if __name__ == '__main__':
    
    import sys
    app = QtWidgets.QApplication(sys.argv)
    
    bm = MedManager()
    
    sys.exit(app.exec_())
    