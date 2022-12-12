import socket
from networkFactor import *
import pickle 

HOST = finalReceiveIp
# HOST = '1.234.23.229'
PORT = finalReceivePort

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen()

finalCount = 0

def displayMsg(rxData):
    print('area: {}'.format(rxData['area']))
    print('first: {}'.format(rxData['first']))
    print('last: {}'.format(rxData['last']))
    print('phone: {}'.format(rxData['phone']))
    print('from: {}'.format(rxData['from']['ip']))
    print('data: {}'.format(rxData['from']['data']))
    for i in range(len(rxData['data'])):
        print('{}: {}'.format(i, rxData['data'][i]))

def serverMain():
    global finalCount
    print('Wait Client connection.')
    client_socket, addr = server_socket.accept()
    print('Connected by', addr)
    data = client_socket.recv(1024)
    if data:
        msg = pickle.loads(data)
        fromData = 'from: final remoteReceiveData.py: {}'.format(msg['first'])
        print('original size: {}'.format(msg['dataSize']))
        print('receiveCount: {}, size: {}'.format(finalCount, len(data)))
        print('Received from', addr, msg['first'])
        client_socket.sendall(fromData.encode())
        
        displayMsg(msg)
        finalCount += 1

    client_socket.close()

def main():
    print('now start. testTcpIpServer.py 2022.11.14 10:04')
    mainCount = 0
    while True:
        serverMain()
        mainCount += 1
        # time.sleep(1)

if __name__ == "__main__":
    main()



