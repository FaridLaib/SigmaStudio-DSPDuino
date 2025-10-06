from PyQt5 import QtCore, QtGui, QtWidgets
import serial  # For communication with ESP32


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(603, 444)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Slider
        self.verticalSlider = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider.setGeometry(QtCore.QRect(360, 120, 41, 161))
        self.verticalSlider.setMinimum(-50)  # Minimum volume in dB
        self.verticalSlider.setMaximum(0)   # Maximum volume in dB
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")

        # Text Display for Volume
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(240, 190, 104, 31))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setReadOnly(True)  # Make it read-only

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 603, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Connect slider to update function
        self.verticalSlider.valueChanged.connect(self.update_volume)

        # Initialize serial communication
        try:
            self.esp32_serial = serial.Serial('COM6', 9600)  # Replace 'COM3' with your ESP32 port
        except serial.SerialException:
            self.esp32_serial = None
            self.textEdit.setText("Failed to connect to ESP32")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Volume Control"))
        self.textEdit.setHtml(_translate("MainWindow", "<p style=\"font-size:14px;\">Volume Control</p>"))

    def update_volume(self, value):
        """Send slider value to ESP32 and update display."""
        # Update the text display
        self.textEdit.setText(f"Volume: {value} dB")

        # Send the value to the ESP32
        if self.esp32_serial:
            command = f"Volume:{value}\n"  # Example command format
            self.esp32_serial.write(command.encode())  # Send the command
        else:
            self.textEdit.setText("ESP32 not connected!")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
