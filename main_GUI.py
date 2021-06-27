from typing import Text
from flask import jsonify
from requests import api
from api_temp_request import GetTemperatureFromApi, requests, json, jsonpickle
from os import system
from power_stove_calculate import Calculation
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui, QtWidgets, _QOpenGLFunctions_2_0
from main import StoveControl
from gui_input import InputGuiValues

""" In the following class, are located GUI elements
    App working with PyQT5 """


class Ui_MainWindow(object):

    qt_text = StoveControl()

    def setupUi(self, MainWindow):

        buttons_connect = StoveControl()

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(9, 4, 181, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 35, 400, 20))
        self.label.setObjectName("label")
        self.label.setFont(QFont("Times New Roman", 12))
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(210, 120, 400, 13))
        self.label_2.setObjectName("label_2")
        self.label_2.setFont(QFont("Times New Roman", 12))
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(210, 210, 1400, 13))
        self.label_3.setObjectName("label_3")
        self.label_3.setFont(QFont("Times New Roman", 12))
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(210, 310, 400, 13))
        self.label_4.setObjectName("label_4")
        self.label_4.setFont(QFont("Times New Roman", 12))
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(770, 10, 400, 50))
        self.label_5.setObjectName("label_5")
        self.label_5.setFont(QFont("Times New Roman", 12))
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(770, 180, 400, 50))
        self.label_6.setObjectName("label_6")
        self.label_6.setFont(QFont("Times New Roman", 12))
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(770, 90, 400, 50))
        self.label_7.setObjectName("label_7")
        self.label_7.setFont(QFont("Times New Roman", 12))
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(10, 180, 181, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(10, 270, 181, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(580, 0, 181, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(580, 80, 181, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(10, 90, 181, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(580, 170, 181, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setObjectName("pushButton_13")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1118, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        input_value = InputGuiValues()

        # connect to db_pg_admin
        try:
            self.pushButton_7.clicked.connect(
                lambda: buttons_connect.connect_to_pgadmin(
                    buttons_connect.api_info.data2,
                    buttons_connect.api_info.data1,
                )
                and self.label.setText("!Pomyślnie połączono z bazą danych!".upper())
            )
        except:
            self.label.setText("!Błąd połączenia z bazą danych!").upper()

        # return day temp info from api
        self.pushButton_8.clicked.connect(
            lambda: buttons_connect.return_temp_from_json(
                buttons_connect.temp_celcius, buttons_connect.api_info.data2
            )
            or self.label_3.setText(str(self.qt_text.api_info.data1) + "°C")
        )

        # return day temp info from api in json
        self.pushButton_9.clicked.connect(
            lambda: buttons_connect.return_json_info(
                buttons_connect.api_info.response_info
            )
            or self.label_4.setText("Json wyświetlany jest w konsoli!!!".upper())
            and self.qt_text.api_click == True
        )
        # power stove auto mode
        self.pushButton_10.clicked.connect(
            lambda: buttons_connect.power_stove_calcution(
                0, buttons_connect.temp_celcius
            )
            or self.label_5.setText(
                "Moc pieca w auto pieca\nustawiona na: "
                + str(self.qt_text.power_calc.temp_calc)
                + "%"
            )
            and self.qt_text.api_click
        )

        # manual stove control
        self.pushButton_11.clicked.connect(
            lambda: (input_value.show_input_temp_dialog())
            or self.label_7.setText(
                "Moc pieca w MANUAL\nustawiona na: "
                + str(self.qt_text.power_calc.temp_calc)
                + "%"
            )
        )
        # put values to db
        try:
            self.pushButton_12.clicked.connect(
                lambda: buttons_connect.put_values_to_db(
                    buttons_connect.api_info.data2,
                    buttons_connect.api_info.data1,
                )
                or self.label_2.setText(
                    "!Poprawnie wpisano dane do bazy danych!".upper()
                )
            )
        except:
            self.label.setText("!Błąd połączenia z bazą danych!").upper()

        # closee app from GUI elements
        self.pushButton_13.clicked.connect(
            lambda: buttons_connect(sys.exit(app.exec_()))
        )

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sterowanie piecem"))
        self.pushButton_7.setText(_translate("MainWindow", "Połącz z bazą danych"))
        self.pushButton_8.setText(_translate("MainWindow", "Temp. W Katowicach"))
        self.pushButton_9.setText(_translate("MainWindow", "Inf. o Temp. W JSON"))
        self.pushButton_10.setText(_translate("MainWindow", "Tryb AUTO ON"))
        self.pushButton_11.setText(_translate("MainWindow", "Tryb Manual ON"))
        self.pushButton_12.setText(_translate("MainWindow", "Zapisanie Temp. do DB"))
        self.pushButton_13.setText(_translate("MainWindow", "Zamknij Aplkację"))
        self.label.setText(_translate("MainWindow", "<-- klik, błąd gdy MySql OFF"))
        self.label_2.setText(_translate("MainWindow", "<-- klik"))
        self.label_3.setText(_translate("MainWindow", "<-- klik"))
        self.label_4.setText(_translate("MainWindow", "<-- klik"))
        self.label_5.setText(_translate("MainWindow", "<-- klik"))
        self.label_6.setText(
            _translate(
                "MainWindow", "Wyłącz aplikację \n przerwij sterowanie pieca z apki"
            )
        )
        self.label_7.setText(_translate("MainWindow", "<-- klik"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
