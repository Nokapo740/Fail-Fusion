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
