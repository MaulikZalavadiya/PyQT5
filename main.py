import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon


def window():
    app = QApplication(sys.argv)
    win = QMainWindow()

    win.setGeometry(1200,300,700,700)
    win.setWindowTitle("maulik patel")
    win.setWindowIcon(QIcon("11.png"))
    # win.setToolTip("Maulik Patel")

    lbl_name = QtWidgets.QLabel(win)
    lbl_name.setText('Enter your name :')
    lbl_name.move(50,50)

    lbl_surname = QtWidgets.QLabel(win)
    lbl_surname.setText("Enter your Surname :")
    lbl_surname.move(50,90)

    txt_name = QtWidgets.QLineEdit(win)
    txt_name.move(200,50)

    txt_surname = QtWidgets.QLineEdit(win)
    txt_surname.move(200,90)

    def clicked(self):
        print("button clicked")
        print('name:'+ txt_name.text())
        print('surname:'+ txt_surname.text())


    btn_save =QtWidgets.QPushButton(win)
    btn_save.setText('Save')
    btn_save.clicked.connect(clicked)
    btn_save.move(200,130)

    win.show()
    sys.exit(app.exec_())


window()