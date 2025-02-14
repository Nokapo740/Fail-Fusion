from PyQt5 import QtCore, QtGui, QtWidgets
import subprocess

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.setStyleSheet("background-color: rgb(255, 238, 238);")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Главный вертикальный компоновщик
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)

        # Создание и добавление виджетов
        self.label = QtWidgets.QLabel("FailFusion")
        self.label.setStyleSheet("font: 75 20pt 'MS Shell Dlg 2'; color: rgb(0, 0, 0);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout.addWidget(self.label)

        self.textBrowser = QtWidgets.QTextBrowser()
        self.textBrowser.setStyleSheet("background-color: rgb(226, 75, 113); selection-color: rgb(177, 255, 52); border-right-color: rgb(0, 0, 0); border-color: rgb(0, 0, 0);")
        self.verticalLayout.addWidget(self.textBrowser)

        # Горизонтальный компоновщик для чекбокса и кнопки
        self.horizontalLayout = QtWidgets.QHBoxLayout()

        self.checkBox = QtWidgets.QCheckBox("Я принимаю правила")
        self.checkBox.setStyleSheet("font: 75 9pt 'MS Shell Dlg 2'; color: rgb(0,0,0);")
        self.horizontalLayout.addWidget(self.checkBox)

        self.pushButton = QtWidgets.QPushButton("Начать работу")
        self.pushButton.setStyleSheet("font: 10pt 'Poor Richard'; background-color: rgb(221, 73, 110); gridline-color: rgb(76, 76, 76);")
        self.horizontalLayout.addWidget(self.pushButton)

        self.verticalLayout.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        # Делаем кнопку неактивной по умолчанию
        self.pushButton.setEnabled(False)

        # Привязываем изменение состояния чекбокса к функции toggle_button
        self.checkBox.stateChanged.connect(self.toggle_button)

        # Привязка метода open_external_file к событию нажатия кнопки
        self.pushButton.clicked.connect(self.open_external_file)

        # Установка текста политики конфиденциальности для textBrowser
        self.textBrowser.setHtml(QtCore.QCoreApplication.translate("MainWindow", """
        <html>
        <body>
        <p style="font-size:10pt; font-weight:400;">Политика конфиденциальности приложения</p>
        <p style="font-size:10pt; font-weight:400;">Приложение собирает и хранит минимально необходимую информацию для обеспечения его функциональности. К такой информации могут относиться данные, предоставленные пользователем при регистрации или использовании сервиса. Личная информация пользователя используется исключительно в рамках предоставления функционала приложения. Мы не раскрываем персональные данные третьим лицам без вашего явного согласия.</p>
        <p style="font-size:10pt; font-weight:400;">Мы прилагаем максимум усилий для обеспечения безопасности ваших данных. Технологии шифрования и другие меры защиты используются для предотвращения несанкционированного доступа к вашей личной информации. Мы можем использовать анонимные, агрегированные данные для улучшения качества и функционала приложения. Эти данные не содержат личной информации и используются исключительно в аналитических целях. Используя приложение, вы подтверждаете свое согласие с нашей политикой конфиденциальности. Мы рекомендуем ознакомиться с правилами перед использованием приложения. В случае сотрудничества с партнерами или сторонними сервисами, мы стремимся гарантировать, что их политика конфиденциальности соответствует нашим стандартам.</p>
        <p style="font-size:10pt; font-weight:400;">Политика конфиденциальности может периодически обновляться. Изменения будут опубликованы в приложении, и вам будет предоставлена возможность ознакомиться с обновленной версией. Вы имеете право запросить доступ, исправление или удаление своих личных данных. Если у вас есть вопросы или замечания относительно политики конфиденциальности, свяжитесь с нами по указанным контактным данным.</p>
        </body>
        </html>6
        """))

    def toggle_button(self):
        self.pushButton.setEnabled(self.checkBox.isChecked())

    def open_external_file(self):
        # Закрытие текущего окна
        self.MainWindow.close()

        # Запуск внешнего файла Python
        subprocess.run(["python", "un2.py"])

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
