import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QRadioButton,QButtonGroup,QLineEdit,QPushButton
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700,300,500,500)
        self.lineedit=QLineEdit(self)
        self.button=QPushButton("Submit",self)
        self.initUI()
    def initUI(self):
       self.lineedit.setGeometry(10,10,200,50)
       self.lineedit.setStyleSheet("font-size:15px;font-family:Arial")
       self.button.setStyleSheet("font-size:25px;font-family:Arial")
       self.button.setGeometry(210,10,100,50)
       self.button.clicked.connect(self.submit)
       self.lineedit.setPlaceholderText("Enter your name")
    def submit(self):
        text=self.lineedit.text()
        print(f"hi!!!!!!!!!!!!{text}")
if __name__=='__main__':
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())