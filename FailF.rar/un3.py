from PyQt5 import QtCore, QtGui, QtWidgets
import os
import shutil
import zipfile
import subprocess

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(255, 238, 238);")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(240, 70, 311, 41))
        self.label.setStyleSheet("font: 16pt \"Tw Cen MT\";")
        self.label.setObjectName("label")

        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(200, 180, 391, 31))
        self.textEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                    "font: 10pt \"MS Shell Dlg 2\";")
        self.textEdit.setObjectName("textEdit")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 520, 91, 31))
        self.pushButton.setStyleSheet("background-color: rgb(226, 75, 113);\n"
                                      "font: 75 9pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(200, 150, 141, 16))
        self.label_2.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(200, 270, 161, 16))
        self.label_3.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")

        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(200, 300, 391, 31))
        self.textEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                      "font: 10pt \"MS Shell Dlg 2\";")
        self.textEdit_2.setObjectName("textEdit_2")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 220, 111, 31))
        self.pushButton_2.setStyleSheet("background-color: rgb(226, 75, 113);\n"
                                        "font: 75 9pt \"MS Shell Dlg 2\";")
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(200, 340, 111, 31))
        self.pushButton_3.setStyleSheet("background-color: rgb(226, 75, 113);\n"
                                        "font: 75 9pt \"MS Shell Dlg 2\";")
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(200, 390, 171, 41))
        self.pushButton_4.setStyleSheet("background-color: rgb(226, 75, 113);\n"
                                        "font: 75 10pt \"MS Shell Dlg 2\";")
        self.pushButton_4.setObjectName("pushButton_4")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Connect 'Обзор...' buttons
        self.pushButton_2.clicked.connect(lambda: self.browse_folder(self.textEdit))
        self.pushButton_3.clicked.connect(lambda: self.browse_folder(self.textEdit_2))

        # Connect 'Начать копирование' button
        self.pushButton_4.clicked.connect(self.backup_files)

        # Connect 'Назад' button
        self.pushButton.clicked.connect(self.close_and_open_un2)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Резервное копирование данных"))
        self.pushButton.setText(_translate("MainWindow", "<- Назад"))
        self.label_2.setText(_translate("MainWindow", "Исходный каталог:"))
        self.label_3.setText(_translate("MainWindow", "Каталог назначения:"))
        self.pushButton_2.setText(_translate("MainWindow", "Обзор..."))
        self.pushButton_3.setText(_translate("MainWindow", "Обзор..."))
        self.pushButton_4.setText(_translate("MainWindow", "Начать копирование"))

    def browse_folder(self, textEdit):
        folder_selected = QtWidgets.QFileDialog.getExistingDirectory()
        if folder_selected:
            textEdit.setText(folder_selected)

    def find_next_backup_number(self, directory, base_name):
        counter = 1
        while True:
            backup_name = f"{base_name} {counter}.zip"
            backup_path = os.path.join(directory, backup_name)
            if not os.path.exists(backup_path):
                return backup_name
            counter += 1

    def backup_files(self):
        source_directory = self.textEdit.toPlainText()
        backup_directory = self.textEdit_2.toPlainText()

        if not os.path.exists(source_directory):
            QtWidgets.QMessageBox.critical(None, "Ошибка", "Исходный каталог не найден.")
            return

        backup_zip_name = self.find_next_backup_number(backup_directory, "Копия")
        backup_zip_path = os.path.join(backup_directory, backup_zip_name)

        backup_subdirectory = os.path.join(backup_directory, "Копия_temp")
        if not os.path.exists(backup_subdirectory):
            os.makedirs(backup_subdirectory)

        files = os.listdir(source_directory)
        for file in files:
            shutil.copy2(os.path.join(source_directory, file), os.path.join(backup_subdirectory, file))

        with zipfile.ZipFile(backup_zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(backup_subdirectory):
                for file in files:
                    zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), backup_subdirectory))
        shutil.rmtree(backup_subdirectory)

        QtWidgets.QMessageBox.information(None, "Резервное копирование", f"Файлы успешно скопированы и архивированы в '{backup_zip_name}'")

    def close_and_open_un2(self):
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
