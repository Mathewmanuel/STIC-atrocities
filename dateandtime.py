#date and time
import datetime
import time

def setalarm(alarmtime):
    print(f"alarm has been set for{alarmtime}")
isrunning=True
while isrunning:
    ctime=datetime.datetime.now().strftime("%H:%M:%S")
    print(ctime)
    time.sleep(1)
    if ctime == alarmtime:
        print("wakeup!!!!!!!!!!!!!!!!!")

if __name__=="__main__":
    alarmtime =input("enter alarmtime as (HH:MM:SS):")
    setalarm(alarmtime)