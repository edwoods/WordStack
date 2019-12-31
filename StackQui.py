# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wordStack.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from WordStack import SolveWordStack, LoadStack

class Ui_MainWindow(object):
    def __init__(self):
        self.btns = []

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(406, 381)
        MainWindow.setFocusPolicy(QtCore.Qt.ClickFocus)
        MainWindow.setAcceptDrops(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_2.setSpacing(0)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setFamily("Courier New")

        for row in range(15):
            a = []
            for col in range(10):
                btn = QtWidgets.QPushButton(self.frame)
                btn.setMaximumSize(QtCore.QSize(22, 22))
                btn.setCheckable(True)
                btn.setObjectName("PB" + str(row))
                btn.setText("")
                btn.setFont(font)

                btn.clicked.connect(lambda state, x=row, y=col: self.onClick(x,y))

                self.gridLayout_2.addWidget(btn, row, col)
                a.append(btn)
            self.btns.append(a)

        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        self.theWords = QtWidgets.QPlainTextEdit(self.frame)
        self.theWords.setObjectName("theWords")
        self.gridLayout_3.addWidget(self.theWords, 0, 2, 2, 1)

        self.horizontalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 406, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionOpen.setShortcut("Ctrl+O")
        self.actionOpen.triggered.connect(self.openWords)
        self.actionEdit = QtWidgets.QAction(MainWindow)
        self.actionEdit.setObjectName("actionEdit")
        self.actionUpdate_words = QtWidgets.QAction(MainWindow)
        self.actionUpdate_words.setObjectName("actionUpdate_words")
        self.actionHilite_Words = QtWidgets.QAction(MainWindow)
        self.actionHilite_Words.setObjectName("actionHilite_Words")
        self.actionRemove_Word = QtWidgets.QAction(MainWindow)
        self.actionRemove_Word.setObjectName("actionRemove_Word")
        self.menuFile.addAction(self.actionOpen)
        self.menuEdit.addAction(self.actionUpdate_words)
        self.menuEdit.addAction(self.actionHilite_Words)
        self.menuEdit.addAction(self.actionRemove_Word)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def SetButton(self, row, col, letter, color):
        self.btns[row][col].setText(letter)


    def onClick(self, row, col):
        print(row, col)

    def openWords(self):
        self.clearWords()
        LoadStack(self)

        SolveWordStack(self)
        print("opening default file")

    def clearWords(self):
        self.theWords.setPlainText("")

    def AddLine(self, line):
        self.theWords.append("\n")
        self.theWords.append(line)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.theWords.setPlainText(_translate("MainWindow", ""))
        # self.pushButton_21.setText(_translate("MainWindow", "a"))
        # self.pushButton_19.setText(_translate("MainWindow", "a"))
        # self.pushButton_18.setText(_translate("MainWindow", "a"))
        # self.pushButton_17.setText(_translate("MainWindow", "a"))
        # self.pushButton_20.setText(_translate("MainWindow", "a"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionEdit.setText(_translate("MainWindow", "Edit"))
        self.actionUpdate_words.setText(_translate("MainWindow", "Update words"))
        self.actionHilite_Words.setText(_translate("MainWindow", "Hilite Words"))
        self.actionRemove_Word.setText(_translate("MainWindow", "Remove Word"))

# button3.setStyleSheet("background-color:rgb(255,0,0)");

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
