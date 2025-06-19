import time

def count(end,start=0):
    for x in range(start,end):
        print(x)
        time.sleep(x)
    print(x)

count(5)