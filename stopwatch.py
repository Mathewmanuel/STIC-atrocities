import sys 
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,QPushButton,QVBoxLayout,QHBoxLayout)
from PyQt5.QtCore import QTimer,QTime,Qt

class stopwatch(QWidget):
    def __init__(self):
        super().__init__()
        self.time=QTime(0,0,0,0)
        self.timelabel=QLabel("00:00:00.00",self)
        self.startbutton=QPushButton("start",self)
        self.stopbutton=QPushButton("stop",self)
        self.resetbutton=QPushButton("reset",self)
        self.timer=QTimer(self)
        self.initUI()
    def initUI(self):
        self.setWindowTitle("StopWatch")
        vbox=QVBoxLayout()
        vbox.addWidget(self.timelabel)
        vbox.addWidget(self.startbutton)
        vbox.addWidget(self.stopbutton)
        vbox.addWidget(self.resetbutton)
        self.setLayout(vbox)
        self.timelabel.setAlignment(Qt.AlignCenter)
        hbox=QHBoxLayout()
        hbox.addWidget(self.startbutton)
        hbox.addWidget(self.stopbutton)
        hbox.addWidget(self.resetbutton)
        vbox.addLayout(hbox)
        self.setStyleSheet("""
                           QPushButton,QLabel{padding:20px;font-weight:bold;font-family:calibri;
                           }
                           
                           QPushButton
                           {font-size:120px;
                           background-color:hsl(200,85%,90%)}
                           QLabel{
                           font-size:120px;
                           background-color:hsl(200,70%,50%)
                           }""")
        self.startbutton.clicked.connect(self.start)
        self.stopbutton.clicked.connect(self.stop)
        self.resetbutton.clicked.connect(self.reset)
        self.timer.timeout.connect(self.updatedisplay)
    def start(self):
        self.timer.start(10)
    def stop(self):
        self.timer.stop()
    def reset(self):
        self.timer.stop()
        self.time=QTime(0,0,0,0)
        self.timelabel.setText(self.formattime(self.time))
    def formattime(self,time):
        hours=time.hour()
        minutes=time.minute()
        seconds=time.second()
        millseconds=time.msec()
        return f"{hours:02}:{minutes:02}:{seconds:02}.{millseconds:02}"
    def updatedisplay(self):
        self.time=self.time.addMSecs(10)
        self.timelabel.setText(self.formattime(self.time))


if __name__=="__main__":
    app=QApplication(sys.argv)
    stopwatch=stopwatch()
    stopwatch.show()
    sys.exit(app.exec_())