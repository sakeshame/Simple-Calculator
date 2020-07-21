from PyQt5 import QtWidgets
from calci import Ui_Calculator


class CalculatorWindow(QtWidgets.QMainWindow, Ui_Calculator):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        # Connect Buttons
        self.pushButton0.clicked.connect(self.digit_pressed)
        self.pushButton00.clicked.connect(self.digit_pressed)
        self.pushButton1.clicked.connect(self.digit_pressed)
        self.pushButton2.clicked.connect(self.digit_pressed)
        self.pushButton3.clicked.connect(self.digit_pressed)
        self.pushButton4.clicked.connect(self.digit_pressed)
        self.pushButton5.clicked.connect(self.digit_pressed)
        self.pushButton6.clicked.connect(self.digit_pressed)
        self.pushButton7.clicked.connect(self.digit_pressed)
        self.pushButton8.clicked.connect(self.digit_pressed)
        self.pushButton9.clicked.connect(self.digit_pressed)

        self.pushButtonC.clicked.connect(self.clear_pressed)
        self.pushButtonDeci.clicked.connect(self.deci_pressed)
        self.pushButtonPercent.clicked.connect(self.percent_pressed)
        self.pushButtonBack.clicked.connect(self.back_pressed)

        self.toolButton_Equal.clicked.connect(self.equal_pressed)
        self.toolButton_Divide.clicked.connect(self.tool_pressed)
        self.toolButton_Minus.clicked.connect(self.tool_pressed)
        self.toolButton_Multi.clicked.connect(self.multi_pressed)
        self.toolButton_Plus.clicked.connect(self.tool_pressed)

    def digit_pressed(self):
        button = self.sender()
        initial=self.lineEdit.text()
        if initial == '0':
            initial = button.text()
        else:
            initial = initial + button.text()
        self.lineEdit.setText(str(initial))

    def deci_pressed(self):
        button = self.sender()
        self.lineEdit.setText(self.lineEdit.text() + '.')

    def percent_pressed(self):
        button = self.sender()
        newlabel = format(float(self.lineEdit.text()) * 0.01, '.15g')
        self.lineEdit.setText(newlabel)

    def clear_pressed(self):
        self.lineEdit.setText(self.lineEdit.text() * 0 + '0')

    def back_pressed(self):
        previous = self.lineEdit.text()
        if len(previous[:]) == 1:
            previous = '0'
        else:
            previous = previous[:-1]
        self.lineEdit.setText(previous)

    def tool_pressed(self):
        button = self.sender()
        tool = self.lineEdit.text() + button.text()
        self.lineEdit.setText(tool)

    def multi_pressed(self):
        mul = self.lineEdit.text() + '*'
        self.lineEdit.setText(mul)

    def equal_pressed(self):
        equal=eval(self.lineEdit.text())
        self.lineEdit.setText(str(equal))