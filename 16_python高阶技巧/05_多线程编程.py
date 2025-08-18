import time
import threading

def sing():
    while True:
        print("sing...")
        time.sleep(1)
def dance():
    while True:
        print("dance...")
        time.sleep(1)

if __name__ =='__main__':
    sing_threading = threading.Thread(target=sing)
    dance_threading = threading.Thread(target=dance)
    sing_threading.start()
    dance_threading.start()

