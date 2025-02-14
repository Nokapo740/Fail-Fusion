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
