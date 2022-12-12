import socket
import time 
from networkFactor import *
from pickleData import *
import pickle 
import random 

HOST = gatewayLocalServerIp  
# HOST = '1.234.23.229'  
PORT = gatewayLocalServerPort 

def sendClient(tx):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((HOST, PORT))
        client_socket.sendall(tx)        
        # client_socket.sendall('Good Mornig'.encode())        
        data = client_socket.recv(1024)
        print('Received', repr(data.decode()))
        client_socket.close()
    except:
        print('server not connected: -h{},-p{}'.format(HOST, PORT))
    finally:
        print('finally next:')

def main():
    mainCount = 0
    while True:
        msg = '{}, {}\r\n'.format(mainCount%10, mainCount)
        txData['from']['data'] = msg 
        # txData['area'] = random.randrange(0, 10)
        txData['rack'] = random.randrange(0, 101)
        txData['status'] = random.randrange(0, 4)
        txData['v37'] = random.randrange(0, 101)
        txData['v74'] = random.randrange(0, 101)
        msg = pickle.dumps(txData)
        sendClient(msg)
        print('sizeof(msg):{}'.format(len(msg)))
        mainCount += 1
        time.sleep(10)

if __name__ == "__main__":
    main()