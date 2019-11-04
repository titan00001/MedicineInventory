'''Initialisation code goes here'''

if __name__ == '__main__':
    from PyQt5 import Qt,QtWidgets
    from main import MedManager
    
    
    import sys
    app = QtWidgets.QApplication(sys.argv)
        
    bm = MedManager()
        
    sys.exit(app.exec_())