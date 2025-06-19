import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QPushButton,QWidget, QHBoxLayout
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.button1=QPushButton("#1")
        self.button2=QPushButton("#2")
        self.button3=QPushButton("#3")
        self.initUI()
    def initUI(self):
        central_widget=QWidget()
        self.setCentralWidget(central_widget)
        hbox=QHBoxLayout()
        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)
        central_widget.setLayout(hbox)
        self.button1.setObjectName("Button1")
        self.button2.setObjectName("Button2")
        self.button3.setObjectName("Button3")
        self.setStyleSheet("""
                           QPushButton{font-size:40px;font-family:Arial;padding:15px 75px;margin:25px;border 3px solid;borderradius 25px;
                           }
                           QPushButton#Button1
                           {
                           background-color:red;
                           }
                           QPushButton#Button2
                           {
                           background-color:green;
                           }
                           QPushButton#Button3
                           {
                           background-color:blue;
                           }QPushButton#Button1:hover
                           {
                           background-color:hsl(122,50%,84%);
                           }
                           QPushButton#Button2:hover
                           {
                           background-color:yellow;
                           }
                           QPushButton#Button3:hover
                           {
                           background-color:orange;
                           }""")
if __name__=='__main__':
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())