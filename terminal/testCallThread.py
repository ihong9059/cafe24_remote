import testThreadClass
import time 

def main():
    myThread = testThreadClass.myThread('hong Thread')
    myThread.daemon = True 
    myThread.start()
    print('callThread test. 2022.11.18 09:10')
    mainCount = 0
    while True:
        print("mainCount: {}".format(mainCount))
        mainCount += 1
        time.sleep(1)


if __name__ == "__main__":
    main()
