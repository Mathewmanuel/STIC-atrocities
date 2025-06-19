import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.cityllabel = QLabel("Enter city name:", self)
        self.cityinput = QLineEdit(self)
        self.getweatherbutton = QPushButton( self)
        self.temperaturelabel = QLabel( self)
        self.emojilabel = QLabel( self)
        self.descriptionlabel = QLabel( self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Weather App")

        vbox = QVBoxLayout()
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

        self.cityllabel.setObjectName("cityllabel")
        self.cityinput.setObjectName("cityinput")
        self.getweatherbutton.setObjectName("getweatherbutton")
        self.temperaturelabel.setObjectName("temperaturelabel")
        self.emojilabel.setObjectName("emojiLabel")
        self.descriptionlabel.setObjectName("descriptionlabel")

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
                font-family: 'Segoe UI Emoji';
            }

            QLabel#descriptionlabel {
                font-size: 50px;
            }
        """)
        self.getweatherbutton.clicked.connect(self.getweather)
    def getweather(self):
        apikey="4fc91fb14187369e577dd1d716db14d5"
        city=self.cityinput.text()
        url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}"
        response=requests.get(url)
        data=response.json()
        print(data)


    def displayerror(self,message):
        pass
    def displayweather(self,data):
        pass
if __name__ == "__main__":
    app = QApplication(sys.argv)
    weatherapp = WeatherApp()
    weatherapp.show()
    sys.exit(app.exec_())
