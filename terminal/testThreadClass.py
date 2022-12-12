import threading 
import time 
import socket
from .networkFactor import * 

class myThread(threading.Thread): 
    def __init__(self, name):
        threading.Thread.__init__(self) 
        self.name = name 
        self.count = 0
        self.ServerIp = gatewayLocalServerIp
        # HOST = '1.234.23.229'
        self.ServerPort = gatewayLocalServerPort       

        self.CloudIp =  cloudServerIp
        self.CloudPort = cloudServerPort

        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((self.ServerIp, self.ServerPort))
        self.server_socket.listen()

    def sendClient(self, tx):
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((self.CloudIp, self.CloudPort))
            client_socket.sendall('Good Mornig'.encode())        
            data = client_socket.recv(1024)
            print('Received from cloud', repr(data.decode()))
            client_socket.close()
        except:
            print('server not connected: -h{},-p{}'.format(self.CloudIp, self.CloudPort))
        finally:
            print('finally next:')


    def serverMain(self):
        print('Wait Client connection.')
        client_socket, addr = self.server_socket.accept()
        print('Connected by', addr)
        data = client_socket.recv(1024)
        if data:
            print('Received from local: ', addr, data.decode())
            client_socket.sendall(data)

            self.sendClient(data)

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
