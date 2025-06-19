import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.citylabel = QLabel("Enter city name:", self)
        self.cityinput = QLineEdit(self)
        self.getweatherbutton = QPushButton("Get Weather", self)
        self.temperaturelabel = QLabel(self)
        self.emojilabel = QLabel(self)
        self.descriptionlabel = QLabel(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Weather App")

        vbox = QVBoxLayout()
        vbox.addWidget(self.citylabel)
        vbox.addWidget(self.cityinput)
        vbox.addWidget(self.getweatherbutton)
        vbox.addWidget(self.temperaturelabel)
        vbox.addWidget(self.emojilabel)
        vbox.addWidget(self.descriptionlabel)
        self.setLayout(vbox)

        self.citylabel.setAlignment(Qt.AlignCenter)
        self.cityinput.setAlignment(Qt.AlignCenter)
        self.temperaturelabel.setAlignment(Qt.AlignCenter)
        self.emojilabel.setAlignment(Qt.AlignCenter)
        self.descriptionlabel.setAlignment(Qt.AlignCenter)

        self.citylabel.setObjectName("citylabel")
        self.cityinput.setObjectName("cityinput")
        self.getweatherbutton.setObjectName("getweatherbutton")
        self.temperaturelabel.setObjectName("temperaturelabel")
        self.emojilabel.setObjectName("emojiLabel")
        self.descriptionlabel.setObjectName("descriptionlabel")

        self.setStyleSheet("""
            QLabel, QPushButton {
                font-family: Calibri;
            }

            QLabel#citylabel {
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
        apikey = "4fc91fb14187369e577dd1d716db14d5"
        city = self.cityinput.text().strip()
        if not city:
            self.displayerror("Please enter a city name.")
            return

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}"
        try:
            response = requests.get(url)
            data = response.json()
            if data.get("cod") == 200:
                self.displayweather(data)
        except requests.exceptions.HTTPError:
            match response.status_code:
                case 400:
                    self.displayerror("poor request reenter")
                case 401:
                    self.displayerror("poor request reenter")
                case 403:
                    self.displayerror("poor request reenter")
                case 404:
                    self.displayerror("poor request reenter")
                case 500:
                    self.displayerror("poor request reenter")
                case 502:
                    self.displayerror("poor request reenter")
                case 503:
                    self.displayerror("poor request reenter")
                case 504:
                    self.displayerror("poor request reenter")
                
        except requests.exceptions.RequestException:
            self.displayerror("Network error. Please try again.")

    def displayweather(self, data):
        temp_k = data["main"]["temp"]
        description = data["weather"][0]["description"]
        emoji = self.getemoji(description)

        temp_c = round(temp_k - 273.15)
        self.temperaturelabel.setText(f"{temp_c}°C")
        self.descriptionlabel.setText(description.capitalize())
        self.emojilabel.setText(emoji)

    def displayerror(self, message):
        self.temperaturelabel.setText("")
        self.descriptionlabel.setText("")
        self.emojilabel.setText("❌")
        self.cityinput.setPlaceholderText(message)

    def getemoji(self, description):
        desc = description.lower()
        if "cloud" in desc:
            return "☁️"
        elif "rain" in desc:
            return "🌧️"
        elif "clear" in desc:
            return "☀️"
        elif "snow" in desc:
            return "❄️"
        elif "storm" in desc or "thunder" in desc:
            return "⛈️"
        elif "mist" in desc or "fog" in desc:
            return "🌫️"
        else:
            return "🌈"

if __name__ == "__main__":
    app = QApplication(sys.argv)
    weatherapp = WeatherApp()
    weatherapp.show()
    sys.exit(app.exec_())
import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.citylabel = QLabel("Enter city name:")
        self.cityinput = QLineEdit()
        self.getweatherbutton = QPushButton("Get Weather")
        self.temperaturelabel = QLabel()
        self.emojilabel = QLabel()
        self.descriptionlabel = QLabel()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Weather App")

        vbox = QVBoxLayout()
        vbox.addWidget(self.citylabel)
        vbox.addWidget(self.cityinput)
        vbox.addWidget(self.getweatherbutton)
        vbox.addWidget(self.temperaturelabel)
        vbox.addWidget(self.emojilabel)
        vbox.addWidget(self.descriptionlabel)
        self.setLayout(vbox)

        for widget in [self.citylabel, self.cityinput, self.temperaturelabel, self.emojilabel, self.descriptionlabel]:
            widget.setAlignment(Qt.AlignCenter)

        self.setStyleSheet("""
            QLabel, QPushButton {
                font-family: Calibri;
            }
            QLabel#citylabel {
                font-size: 40px;
                font-style: italic;
            }
            QLineEdit {
                font-size: 40px;
            }
            QPushButton {
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

        self.citylabel.setObjectName("citylabel")
        self.cityinput.setObjectName("cityinput")
        self.getweatherbutton.setObjectName("getweatherbutton")
        self.temperaturelabel.setObjectName("temperaturelabel")
        self.emojilabel.setObjectName("emojiLabel")
        self.descriptionlabel.setObjectName("descriptionlabel")

        self.getweatherbutton.clicked.connect(self.getweather)

    def getweather(self):
        apikey = "4fc91fb14187369e577dd1d716db14d5"
        city = self.cityinput.text().strip()

        if not city:
            self.displayerror("Please enter a city name.")
            return

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}"

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            if data.get("cod") == 200:
                self.displayweather(data)
            else:
                self.displayerror(data.get("message", "Error retrieving data."))

        except requests.exceptions.HTTPError as err:
            self.displayerror(f"HTTP error: {err.response.status_code}")
        except requests.exceptions.RequestException:
            self.displayerror("Network error. Please try again.")

    def displayweather(self, data):
        temp_k = data["main"]["temp"]
        description = data["weather"][0]["description"]
        emoji = self.getemoji(description)

        temp_c = round(temp_k - 273.15)
        self.temperaturelabel.setText(f"{temp_c}°C")
        self.descriptionlabel.setText(description.capitalize())
        self.emojilabel.setText(emoji)

    def displayerror(self, message):
        self.temperaturelabel.clear()
        self.descriptionlabel.clear()
        self.emojilabel.setText("❌")
        self.cityinput.setPlaceholderText(message)

    def getemoji(self, description):
        desc = description.lower()
        if "cloud" in desc:
            return "☁️"
        elif "rain" in desc:
            return "🌧️"
        elif "clear" in desc:
            return "☀️"
        elif "snow" in desc:
            return "❄️"
        elif "storm" in desc or "thunder" in desc:
            return "⛈️"
        elif "mist" in desc or "fog" in desc:
            return "🌫️"
        else:
            return "🌈"

if __name__ == "__main__":
    app = QApplication(sys.argv)
    weatherapp = WeatherApp()
    weatherapp.show()
    sys.exit(app.exec_())
