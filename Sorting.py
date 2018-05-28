import sys
from PySide import QtGui,QtCore

import os

from PySide.QtCore import Qt
from PySide.QtGui import QShortcut, QKeySequence


class LayoutTest(QtGui.QWidget):
    def __init__(self):
        super(LayoutTest, self).__init__()
        self.first_box  = QtGui.QVBoxLayout()
        self.path = "Input/"
        self.reworkpath = "Output/Rejected/"
        self.donepath = "Output/Approved/"
        self.j=0
        self.zvbox = QtGui.QVBoxLayout()

        vbox = QtGui.QVBoxLayout()
        vbox.addLayout(self.first_box)
        self.files = os.listdir(self.path)
        self.setLayout(vbox)

        self.first_view()

        self.setGeometry(300, 200, 400, 300)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            self.close()

    def first_view(self):
        self.pic = QtGui.QLabel(self)
        self.pic.setPixmap(QtGui.QPixmap("%s%s" % (self.path, self.files[self.j])))
       

        self.next1 = QtGui.QPushButton("Approved")
        self.next2 = QtGui.QPushButton("Rejected")
        self.undoButton = QtGui.QPushButton("Undo")
        self.next1.clicked.connect(self.nextImage)
        self.next2.clicked.connect(self.copyImage)
        self.undoButton.clicked.connect(self.undo)
        self.first_box.addWidget(self.next1)
        self.first_box.addWidget(self.next2)
        self.first_box.addWidget(self.undoButton)
        self.first_box.addWidget(self.pic)
        self.next1.setShortcut(QtGui.QKeySequence("Y"))
        self.next2.setShortcut(QtGui.QKeySequence("N"))
        self.undoButton.setShortcut(QtGui.QKeySequence("Z"))

    def nextImage(self):
        os.rename("%s%s" % (self.path, self.files[self.j]), "%s%s" % (self.donepath, self.files[self.j]))
        self.j = self.j + 1
        self.pic.setPixmap(QtGui.QPixmap("%s%s" % (self.path, self.files[self.j])))

    def copyImage(self):
        os.rename("%s%s" % (self.path, self.files[self.j]), "%s%s" % (self.reworkpath, self.files[self.j]))
        self.j = self.j + 1
        self.pic.setPixmap(QtGui.QPixmap("%s%s" % (self.path, self.files[self.j])))

    def undo(self):
        imageinquestion = self.j - 1
        print imageinquestion
        try:
            os.rename("%s%s" % (self.reworkpath, self.files[imageinquestion]),"%s%s" % (self.path, self.files[imageinquestion]))
            self.pic.setPixmap(QtGui.QPixmap("%s%s" % (self.path, self.files[imageinquestion])))
            self.j = self.j - 1
        except:
            os.rename("%s%s" % (self.donepath, self.files[imageinquestion]),"%s%s" % (self.path, self.files[imageinquestion]))
            self.pic.setPixmap(QtGui.QPixmap("%s%s" % (self.path, self.files[imageinquestion])))
            self.j = self.j - 1



def run():

    app = QtGui.QApplication(sys.argv)
    ex = LayoutTest()
    ex.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    run()
