import threading 
import time 
from . import var  

class timeout(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self) 
        self.name = name 
        self.count = 0
        print('now start timeout Thread. 2022.11.25')



    def run(self):
        while True:
            # print('timeout Thread: {}'.format(self.count))
            self.count += 1
            if var.connectionCountdown:
                var.connectionCountdown -= 1
                # print('connectionCount:{}'.format(var.connectionCountdown))
            else:
                print('Time out db connection')
            time.sleep(1)


def main():
    print('now start timeout Thread main. 2022.11.25')
    myThread = timeout('timeout Thread')
    myThread.daemon = True
    myThread.start()

    mainCount = 0

    while True:
        print('threadMain: {}'.format(mainCount))
        mainCount += 1
        time.sleep(1)

if __name__ == "__main__":
    main()