from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import subprocess
from PIL import Image
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 599)
        MainWindow.setStyleSheet("background-color: rgb(255, 238, 238);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(130, 190, 261, 101))
        self.pushButton_4.setStyleSheet("background-color: rgb(226, 75, 113);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 520, 91, 31))
        self.pushButton.setStyleSheet("background-color: rgb(226, 75, 113);\n"
"font: 75 9pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(340, 80, 131, 41))
        self.label.setStyleSheet("font: 16pt \"Tw Cen MT\";")
        self.label.setObjectName("label")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(130, 300, 261, 101))
        self.pushButton_5.setStyleSheet("background-color: rgb(226, 75, 113);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(400, 190, 261, 101))
        self.pushButton_6.setStyleSheet("background-color: rgb(226, 75, 113);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(400, 300, 261, 101))
        self.pushButton_7.setStyleSheet("background-color: rgb(226, 75, 113);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.pushButton_7.setObjectName("pushButton_7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_4.setText(_translate("MainWindow", "Конвертировать в PNG"))
        self.pushButton.setText(_translate("MainWindow", "<- Назад"))
        self.label.setText(_translate("MainWindow", "Конвертатор"))
        self.pushButton_5.setText(_translate("MainWindow", "Конвертировать в RAW"))
        self.pushButton_6.setText(_translate("MainWindow", "Конвертировать в PDF"))
        self.pushButton_7.setText(_translate("MainWindow", "Конвертировать в JPG"))
        self.pushButton_4.clicked.connect(self.convert_to_png)
        self.pushButton_5.clicked.connect(self.convert_to_raw)
        self.pushButton_6.clicked.connect(self.convert_to_pdf)
        self.pushButton_7.clicked.connect(self.convert_to_jpg)
        self.pushButton.clicked.connect(self.open_back)

    def convert_to_png(self):
        file_path, _ = QFileDialog.getOpenFileName(None, "Выберите файл для конвертации", "", "All Files (*)")
        if file_path:
            save_path, _ = QFileDialog.getSaveFileName(None, "Сохранить как PNG", "", "PNG Files (*.png)")
            if save_path:
                try:
                    img = Image.open(file_path)
                    img.save(save_path, 'PNG')
                    print(f"Saved as: {save_path}")
                except Exception as e:
                    print(f"Ошибка при конвертации в PNG: {e}")
    def convert_to_raw(self):
        file_path, _ = QFileDialog.getOpenFileName(None, "Выберите файл для конвертации", "", "All Files (*)")
        if file_path:
            save_path, _ = QFileDialog.getSaveFileName(None, "Сохранить как RAW", "", "RAW Files (*.raw)")
            if save_path:
                # Perform conversion here (subprocess or any other method)
                # For demonstration, let's print the paths (replace this with your conversion logic)
                print(f"Converting {file_path} to RAW and saving at {save_path}")

    def convert_to_pdf(self):
        file_path, _ = QFileDialog.getOpenFileName(None, "Выберите файл для конвертации", "", "All Files (*)")
        if file_path:
            save_path, _ = QFileDialog.getSaveFileName(None, "Сохранить как PDF", "", "PDF Files (*.pdf)")
            if save_path:
                # Perform conversion here (subprocess or any other method)
                # For demonstration, let's print the paths (replace this with your conversion logic)
                print(f"Converting {file_path} to PDF and saving at {save_path}")

    def convert_to_jpg(self):
        file_path, _ = QFileDialog.getOpenFileName(None, "Выберите файл для конвертации", "", "All Files (*)")
        if file_path:
            save_path, _ = QFileDialog.getSaveFileName(None, "Сохранить как JPG", "", "JPG Files (*.jpg)")
            if save_path:
                try:
                    img = Image.open(file_path)
                    img.convert('RGB').save(save_path, 'JPEG')
                    print(f"Saved as: {save_path}")
                except Exception as e:
                    print(f"Ошибка при конвертации в JPG: {e}")

    def open_back(self):
        self.MainWindow.close()
        subprocess.run(["python", "un2.py"])

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
