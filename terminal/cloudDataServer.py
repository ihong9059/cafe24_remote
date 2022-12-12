import threading 
import time 
import socket
from .networkFactor import * 
import pickle 
import requests

class myThread(threading.Thread): 
    def __init__(self, name):
        threading.Thread.__init__(self) 
        self.name = name 
        self.count = 0
        self.ServerIp = cloudServerIp
        # HOST = '1.234.23.229'
        self.ServerPort = cloudServerPort       

        self.webServerIp =  finalReceiveIp
        self.webServerPort = finalReceivePort

        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((self.ServerIp, self.ServerPort))
        self.server_socket.listen()

    def callCreateDb(self, data):
        dbData = '{"area": %d, "rack": %d, "status": %d, "v37": %d, "v74": %d}' % \
        (data['area'], data['rack'], data['status'], data['v37'], data['v74'])
        # dbData = '{"area": %d, "rack": %d}' % (data['area'], data['rack'])
        # print('This is callCreateDb')
        # txData = 'http://1.234.23.229:5100/test/{}/{}'.format('create', dbData)
        txData = 'http://127.0.0.1:5100/test/{}/{}'.format('create', dbData)
        ack = requests.get(txData)
        print(ack)

    def callTest(self, tx):
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((self.webServerIp, self.webServerPort))

            txData = pickle.dumps(tx)   
            client_socket.sendall(txData)        
            data = client_socket.recv(1024)
            print('Received from final:', repr(data.decode()))
            client_socket.close()
            self.callCreateDb(tx)

        except:
            print('server not connected: -h{},-p{}'.format(self.webServerIp, self.webServerPort))
        finally:
            print('finally next:')

    def sendClient(self, tx):
        try:
            # self.callTest(tx) #for monitoring
            print('Call create db +++++++++++++++++++++++')
            self.callCreateDb(tx)
            print('--------------- end of create db')
        except:
            print('server not connected: -h{},-p{}'.format(self.webServerIp, self.webServerPort))
        finally:
            print('finally next:')


    def serverMain(self):
        print('Wait Client connection.')
        client_socket, addr = self.server_socket.accept()
        print('Connected by', addr)
        data = client_socket.recv(1024)
        try:
            if data:
                msg = pickle.loads(data)
                msg['dataSize'] = len(data)
                fromData = 'from: cloudDataServer.py by {}'.format(msg['last'])
                print('Received from local: ', addr)
                client_socket.sendall(fromData.encode())

                self.sendClient(msg)
        except:
            print('************* Error in pickle data **************')

        client_socket.close()



    def run(self): 
        try: 
            while True: 
                print('running:{}, Count:{} '.format(self.name, self.count))
                self.serverMain()
                self.count += 1 
                # time.sleep(1)
        finally: 
            print('ended') 

def main():
    print('now start testThread. 2022.11.14 10:04')
    t1 = myThread('Thread 1') 
    t1.daemon = True 
    t1.start() 

    mainCount = 0

    while True:
        print('threadMain: {}'.format(mainCount))
        mainCount += 1
        time.sleep(1)

if __name__ == "__main__":
    main()
