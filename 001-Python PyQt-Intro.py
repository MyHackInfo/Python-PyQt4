'''
    #### Python PyQt 4 GUI ####
    -This pyqt4 module use for create pretty osme gui interface application.
    -Its give lots of feature that pretty-handy instend tkinter.
    -Its not need lots of code instend tkinter.


    ## Install
        - pip install pyqt4

'''

import sys
import PyQt4

app = PyQt4.QtGui.QApplication(sys.argv)

# Create window object with Qwindget()
window = PyQt4.QtGui.QWidget()

# Use window object for geometry and Title
window.setGeometry(50,50,500,300)
window.setWindowTitle(" Python PyQt")

# This show() use for show pyqt window
window.show()
