from PyQt5 import QtCore, QtGui, QtWidgets
import subprocess

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(800, 600)  # Set fixed size
        MainWindow.setStyleSheet("background-color: rgb(255, 238, 238);")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(340, 70, 121, 31))
        self.label.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";\n"
                                 "color: rgb(0, 0, 0);")
        self.label.setObjectName("label")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 160, 341, 161))
        self.pushButton.setStyleSheet("background-color: rgb(221, 73, 110);\n"
                                      "font: 75 16pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(400, 160, 341, 161))
        self.pushButton_2.setStyleSheet("background-color: rgb(221, 73, 110);\n"
                                        "font: 75 16pt \"MS Shell Dlg 2\";")
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(50, 330, 691, 161))
        self.pushButton_3.setStyleSheet("background-color: rgb(221, 73, 110);\n"
                                        "font: 75 16pt \"MS Shell Dlg 2\";")
        self.pushButton_3.setObjectName("pushButton_3")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.open_ser)
        # Привязка метода open_converter к событию нажатия кнопки "Конвертатор"
        self.pushButton_2.clicked.connect(self.open_converter)

        # Привязка метода open_backup к событию нажатия кнопки "Резервное копирование данных"
        self.pushButton_3.clicked.connect(self.open_backup)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "FailFusion"))
        self.pushButton.setText(_translate("MainWindow", "Мониторинг"))
        self.pushButton_2.setText(_translate("MainWindow", "Конвертатор"))
        self.pushButton_3.setText(_translate("MainWindow", "Резервное копирование данных"))
        
    def open_ser(self):
        self.MainWindow.close()
        subprocess.run(["python", "2.py"])
    # Функция, вызываемая при нажатии кнопки "Конвертатор"
    def open_converter(self):
        self.MainWindow.close()
        subprocess.run(["python", "un4.py"])

    # Функция, вызываемая при нажатии кнопки "Резервное копирование данных"
    def open_backup(self):
        self.MainWindow.close()
        subprocess.run(["python", "un3.py"])



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
