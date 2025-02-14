from PyQt5 import QtCore, QtGui, QtWidgets
import subprocess

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(800, 592)  # Set fixed size

        MainWindow.setStyleSheet("background-color: rgb(255, 238, 238);")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(340, 50, 121, 41))
        self.label.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";\n" "color: rgb(0, 0, 0);")
        self.label.setObjectName("label")

        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(140, 130, 531, 291))
        self.textBrowser.setStyleSheet("background-color: rgb(226, 75, 113);\n"
                                       "selection-color: rgb(177, 255, 52);\n"
                                       "border-right-color: rgb(0, 0, 0);\n"
                                       "border-color: rgb(0, 0, 0);")
        self.textBrowser.setObjectName("textBrowser")

        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(330, 440, 151, 31))
        self.checkBox.setStyleSheet("font: 75 9pt \"MS Shell Dlg 2\";\n" "color: rgb(0,0,0);")
        self.checkBox.setObjectName("checkBox")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(330, 490, 141, 31))
        self.pushButton.setStyleSheet("font: 10pt \"Poor Richard\";\n"
                                      "background-color: rgb(221, 73, 110);\n"
                                      "gridline-color: rgb(76, 76, 76);")
        self.pushButton.setObjectName("pushButton")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Делаем кнопку неактивной по умолчанию
        self.pushButton.setEnabled(False)

        # Привязываем изменение состояния чекбокса к функции toggle_button
        self.checkBox.stateChanged.connect(self.toggle_button)

        # Привязка метода open_external_file к событию нажатия кнопки
        self.pushButton.clicked.connect(self.open_external_file)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "FailFusion"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">    </span></p>\n"
            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Политика конфиденциальности приложения</span></p>\n"
            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Приложение собирает и хранит минимально необходимую информацию для обеспечения его функциональности. К такой информации могут относиться данные, предоставленные пользователем при регистрации или использовании сервиса. Личная информация пользователя используется исключительно в рамках предоставления функционала приложения. Мы не раскрываем персональные данные третьим лицам без вашего явного согласия.</span><span style=\" font-size:10pt; font-weight:600;\">:</span><span style=\" font-size:10pt;\"> Мы прилагаем максимум усилий для обеспечения безопасности ваших данных. Технологии шифрования и другие меры защиты используются для предотвращения несанкционированного доступа к вашей личной информации. Мы можем использовать анонимные, агрегированные данные для улучшения качества и функционала приложения. Эти данные не содержат личной информации и используются исключительно в аналитических целях. Используя приложение, вы подтверждаете свое согласие с нашей политикой конфиденциальности. Мы рекомендуем ознакомиться с правилами перед использованием приложения. В случае сотрудничества с партнерами или сторонними сервисами, мы стремимся гарантировать, что их политика конфиденциальности соответствует нашим стандартам.</span></p>\n"
            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\"> Политика конфиденциальности может периодически обновляться. Изменения будут опубликованы в приложении, и вам будет предоставлена возможность ознакомиться с обновленной версией. Вы имеете право запросить доступ, исправление или удаление своих личных данных. Если у вас есть вопросы или замечания относительно политики конфиденциальности, свяжитесь с нами по указанным контактным данным.</span></p>\n"
            "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p></body></html>"))
        self.checkBox.setText(_translate("MainWindow", "Я принимаю правила"))
        self.pushButton.setText(_translate("MainWindow", "Начать работу"))

    def open_external_file(self):
        # Закрытие текущего окна
        self.MainWindow.close()

        # Запуск внешнего файла Python
        subprocess.run(["python", "un2.py"])

    # Функция для переключения состояния кнопки в зависимости от чекбокса
    def toggle_button(self):
        self.pushButton.setEnabled(self.checkBox.isChecked())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


from PyQt5 import QtCore, QtGui, QtWidgets
import psutil
import GPUtil
import platform
import subprocess

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(255, 238, 238);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(250, 30, 301, 51))
        self.label_title.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")

        self.label_cpu = QtWidgets.QLabel(self.centralwidget)
        self.label_cpu.setGeometry(QtCore.QRect(50, 120, 700, 31))
        self.label_cpu.setObjectName("label_cpu")

        self.label_cpu_usage = QtWidgets.QLabel(self.centralwidget)
        self.label_cpu_usage.setGeometry(QtCore.QRect(50, 180, 700, 31))
        self.label_cpu_usage.setObjectName("label_cpu_usage")

        self.label_gpu = QtWidgets.QLabel(self.centralwidget)
        self.label_gpu.setGeometry(QtCore.QRect(50, 240, 700, 31))
        self.label_gpu.setObjectName("label_gpu")

        self.label_memory = QtWidgets.QLabel(self.centralwidget)
        self.label_memory.setGeometry(QtCore.QRect(50, 300, 700, 31))
        self.label_memory.setObjectName("label_memory")

        self.label_disk = QtWidgets.QLabel(self.centralwidget)
        self.label_disk.setGeometry(QtCore.QRect(50, 360, 700, 31))
        self.label_disk.setObjectName("label_disk")

        self.pushButton_back = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_back.setGeometry(QtCore.QRect(50, 520, 91, 31))
        self.pushButton_back.setStyleSheet("background-color: rgb(221, 73, 110);\n"
                                           "font: 75 9pt \"MS Shell Dlg 2\";")
        self.pushButton_back.setObjectName("pushButton_back")
        self.pushButton_back.hide()

        self.pushButton_view_code = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_view_code.setGeometry(QtCore.QRect(300, 300, 201, 51))
        self.pushButton_view_code.setStyleSheet("background-color: rgb(221, 73, 110);\n"
                                               "font: 75 12pt \"MS Shell Dlg 2\";")
        self.pushButton_view_code.setObjectName("pushButton_view_code")
        self.pushButton_view_code.setText("Анализ системы")
        self.pushButton_back.clicked.connect(self.open_back)
        self.pushButton_view_code.clicked.connect(self.show_system_info)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "System Monitor"))
        self.label_title.setText(_translate("MainWindow", "Системная информация"))
        self.pushButton_back.setText(_translate("MainWindow", "Назад"))

    def show_system_info(self):
        self.update_system_info()
        self.pushButton_view_code.hide()
        self.pushButton_back.show()

    def update_system_info(self):
        processor_info = platform.processor()
        self.label_cpu.setText(f"<b>Процессор:</b> {processor_info}")

        cpu_usage = psutil.cpu_percent()
        self.label_cpu_usage.setText(f"<b>Загрузка CPU:</b> {cpu_usage}%")

        gpus = GPUtil.getGPUs()
        gpu_info = ""
        for gpu in gpus:
            gpu_info += f"<b>GPU {gpu.id}:</b> {gpu.name}, Загрузка: {gpu.load*100:.2f}%, " \
                        f"Память: {gpu.memoryTotal/1000:.2f}GB/{gpu.memoryFree/1000:.2f}GB\n"

        self.label_gpu.setText(f"<b>Графические процессоры:</b>\n{gpu_info}")

        mem_info = psutil.virtual_memory()
        self.label_memory.setText(f"<b>Озу:</b> Всего {self.bytes_to_gb(mem_info.total)}, "
                                  f"Доступно {self.bytes_to_gb(mem_info.available)}")

        disk_info = psutil.disk_usage('/')
        self.label_disk.setText(f"<b>Диск:</b> Всего {self.bytes_to_gb(disk_info.total)}, "
                                f"Доступно {self.bytes_to_gb(disk_info.free)}")

    def bytes_to_gb(self, bytes):
        gb = bytes / (1024 ** 3)
        return f"{gb:.2f} GB"
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


