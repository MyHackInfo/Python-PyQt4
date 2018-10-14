'''

    ## Use PyQt with Oops (Object Oriented) ##

    ## Use Button

    ## Use Button for Function Perform.
    
    

'''

import sys
from PyQ4 import QtGui , QtCore

class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window,self).__init__()
        self.setGeometry(50,50,500,300)
        self.setWindowTitle("Python PyQt")
        self.setWindowIcon(QtGui.QIcon('pythonlogo.png'))
        self.home()


    def home(self):
        #1-Create object of btn.
        btn=QtGui.QPushButton("Quit",self)
        # 2-Event perform on btn.        
        #old->#btn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        btn.clicked.connect(self.close_app) # Call close_app function.
        # 3-Resize btn.
          #->btn.resize(btn.minimumSizeHind())
          #->btn.resize(btn.sizeHind())
        btn.resize(100,100)
        # 4-Move btn.
        btn.move(100,100)
        # Show the Window
        self.show()

    def close_app(self):
        sys.exit()


def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

run()
