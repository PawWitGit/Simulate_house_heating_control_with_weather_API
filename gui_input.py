from PyQt5 import QtCore, QtGui, QtWidgets, _QOpenGLFunctions_2_0
from main import StoveControl


class InputGuiValues(QtWidgets.QWidget, StoveControl):

    input_values = StoveControl()

    def __init__(self):
        super().__init__()
        self.btn = QtWidgets.QPushButton("Podaj moc na której ma pracować piec", self)
        self.btn.move(0, 20)
        self.btn.clicked.connect(self.show_input_temp_dialog)

        self.text_name = QtWidgets.QLineEdit(self)
        self.text_name.move(100, 22)
        self.text_name.setPlaceholderText("% mocy pieca: ")

        self.setGeometry(1100, 370, 300, 50)
        self.setWindowTitle("Praca pieca w trybie manual")

    def show_input_temp_dialog(self):
        val_limit = 101
        while val_limit > 100:

            val, result = QtWidgets.QInputDialog.getText(
                self,
                "",
                "Podaj wartość mocy w %, piec czeka na komendę, jeśli chcesz wyjść wpisz wartość <=100",
            )
            if result == True:
                self.text_name.setText(val)
                self.input_values.power_calc.temp_calc = val
                val_limit = int(val)
                if val_limit <= 100:
                    print(
                        "Moc pieca w trybie Manual ustawiona na: ".upper(),
                        self.input_values.power_calc.temp_calc,
                        "%",
                    )
                else:
                    print("Podałeś liczbę spoza zakresu, wpisz ponownie!".upper())
