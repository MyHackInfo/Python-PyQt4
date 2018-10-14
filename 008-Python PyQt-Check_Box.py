'''

    ## 002->Use PyQt with Oops (Object Oriented) ##
    ## 003->Use Button.
    ## 004->Use Button for Function Perform.
    ## 005->Create Menubar.
    ## 006->Create Toolbar.



'''

import sys
from PyQ4 import QtGui , QtCore

class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window,self).__init__()
        self.setGeometry(50,50,500,300)
        self.setWindowTitle("Python PyQt")
        self.setWindowIcon(QtGui.QIcon('pythonlogo.png'))


        # create submenu Action .
        extractAction = QtGui.QAction("Help",self)
        extractAction.setShortcut("Ctrl+H")
        extractAction.setStatusTip('Help Your')
        extractAction.triggered.connect(self.help)
        sefl.statusBar()

        # Create maiMenu object of menuBar class
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(extractAction)



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

        extractAction = QtGui.QAction(QtGui.QIcon('jio.png'), 'Flee the Scene',self)
        extractAction.triggered.connect(self.close_app)

        self.tooBar = self.addToolBar("Extraction")
        self.Toolbar.addAction(extractAction)

        checkBox = QtGui.QCheckBox('Enlarge Window',self)
        checkBox.move(100,35)
        checkBox.stateChanged.connect(self.enlarge_window)

        self.show()
    def enlarge_window(self,state):
        if state == QtCore.Qt.Checked:
            self.setGeometry(50,50,1000,600)
        else:
            self.setGeometry(50,50,500,300)

    def close_app(self):
        choice=QtGui.QMessageBox.question(self,'Extract!',"Get into the chopper:",
                                        QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            Print("You are die")
            sys.exit()

    def help(self):
        print('This is avaible on online')




def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

run()
