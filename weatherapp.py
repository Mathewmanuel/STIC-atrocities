import sys
import requests
from PyQt5.QtWidgets import (QApplication,QWidget,QLabel,QLineEdit,QPushButton,QVBoxLayout)
from PyQt5.QtCore import Qt
class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.cityllabel=QLabel("Enter city name:",self)
        self.cityinput=QLineEdit(self)
        self.getweatherbutton=QPushButton("Get Weather",self)
        self.temperaturelabel=QLabel("30°C",self)
        self.emojilabel=QLabel("☀️",self)
        self.descriptionlabel=QLabel("Sunny",self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Weather App")
        vbox=QVBoxLayout()
        vbox.addWidget(self.cityllabel)
        vbox.addWidget(self.cityinput)
        vbox.addWidget(self.getweatherbutton)
        vbox.addWidget(self.temperaturelabel)
        vbox.addWidget(self.emojilabel)
        vbox.addWidget(self.descriptionlabel)
        self.setLayout(vbox)
        self.cityllabel.setAlignment(Qt.AlignCenter)
        self.cityinput.setAlignment(Qt.AlignCenter)
        self.temperaturelabel.setAlignment(Qt.AlignCenter)
        self.emojilabel.setAlignment(Qt.AlignCenter)
        self.descriptionlabel.setAlignment(Qt.AlignCenter)

        self.cityllabel.setObjectName("citylabel")
        self.cityinput.setObjectName("cityinput")
        self.getweatherbutton.setObjectName("getweatherbutton")
        self.temperaturelabel.setObjectName("temperature")
        self.emojilabel.setObjectName("emoji")
        self.descriptionlabel.setObjectName("description")

        self.setStyleSheet("""
            QLabel, QPushButton {
                font-family: Calibri;
            }

            QLabel#cityllabel {
                font-size: 40px;
                font-style: italic;
            }

            QLineEdit#cityinput {
                font-size: 40px;
            }

            QPushButton#getweatherbutton {
                font-size: 30px;
                font-weight: bold;
            }

            QLabel#temperaturelabel {
                font-size: 75px;
            }

            QLabel#emojiLabel {
                font-size: 100px;
                font-family: Segoe UI Emoji;
            }

            QLabel#descriptionlabel {
                font-size: 50px;
            }
        """)

if __name__=="__main__":
    app=QApplication(sys.argv)
    weatherapp=WeatherApp()
    weatherapp.show()
    sys.exit(app.exec_())