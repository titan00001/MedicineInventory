import sqlite3

class MDdatabase:
    
    def __init__(self):
        
        global record
        global conn 
        global c 
        
        conn = sqlite3.connect('MedList.db')
        c = conn.cursor()
        c.execute('CREATE TABLE IF NOT EXISTS MedCom_list (CommonName TEXT PRIMARY KEY, ManufacturingDate TEXT, Price INT);')
        c.execute('CREATE TABLE IF NOT EXISTS MedSc_list (CommonName TEXT PRIMARY KEY, GenericName TEXT, ExpiryDate TEXT, Quantity INT);')
        c.execute('CREATE TABLE IF NOT EXISTS Cust_list (CustomerName TEXT PRIMARY KEY, DoctorName TEXT, Date TEXT);')
        
    
    def inputCommInfo(self,n,dt,p):
        '''insert given commercial info to database'''
        c.execute('INSERT INTO MedCom_list VALUES (?,?,?)',(n,dt,p))
        conn.commit()
        
    def inputScienInfo(self,commonName,genericName,exp_date,qty): 
        '''insert given scientific info to database''' 
        c.execute('INSERT INTO MedSc_list VALUES (?,?,?,?)',(commonName,genericName,exp_date,qty))
        conn.commit()
        
    def inputCustInfo(self,name,doc_name,phone):
        '''insert given customer info to database'''
        c.execute('INSERT INTO Cust_list VALUES (?,?,?)',(name,doc_name,phone))
        conn.commit()
        
    def getCommercialNameList(self):
        '''fetch all the names of medicine in database and returns as list'''
        c.execute('SELECT CommonName FROM MedCom_list')
        CommInfoList = c.fetchall()
        commonNameList = []
        for medicine in CommInfoList:
            commonNameList.append(medicine[0])
            
        return commonNameList
    
    def getCommercialInfo(self,c_Name):
        '''fetch the commercial info and returns as tuple on getting the common name of medicine'''
        c.execute('SELECT * FROM MedCom_List WHERE CommonName = ?',(c_Name,))    
        info = c.fetchone()
        if info != None:
            return info
        else :
            return (c_Name,'','') 
        
    
    def getScientificInfo(self,commonName):
        '''fetch the scientific info and returns as tuple on getting the common name of medicine'''
        c.execute('SELECT * FROM MedSc_List WHERE CommonName = ?',(commonName,))
        info = c.fetchone()
        if info != None:
            return info
        else :
            return (commonName,'Not found','Not-found','Not found')
        #c.execute('UPDATE booklist1 SET Quantity =? WHERE Title =?',())
        
    
    def DBexit(self):
        '''close the connection'''
        conn.close()
        
        
'''if __name__ == '__main__':
        b = MDdatabase()
        n = 'Metro'
        l=b.getScientificInfo(n)
        commonName = l[0]
        mfg_date = l[1]
        price = l[2]
        print(l)
        print('l1 is',l[1])
        print('l2 is',l[2])
        print('l3 is',l[3])'''