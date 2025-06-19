import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QLabel,QWidget,QPushButton, QCheckBox

from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Maddy's GUI")
        self.setGeometry(700,300,500,500)
        self.setWindowIcon(QIcon("pexels-chetanvlad-1595655.jpg"))
        self.initUI()
        label=QLabel("Hello",self)
        self.checkbox=QCheckBox("do you like fishes",self)
        label.setFont(QFont("Arial",30))
        label.setGeometry(50,50,300,300)
        label.setStyleSheet("color:blue;font-weight:bold;font-style:italic;")
        label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        label1=QLabel(self)
        label1.setGeometry(0,0,100,100)
        pixmap=QPixmap("pexels-chetanvlad-1595655.jpg")
        label1.setPixmap(pixmap)
        label1.setScaledContents(True)
    def initUI(self):
       self.checkbox.setStyleSheet("Font-size:30px;font-family:Arial;")
    def onclick(self):
        print("boooooooooooo")
        self.button.setText("Clicked")
      
def main():
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__=="__main__":
    main()