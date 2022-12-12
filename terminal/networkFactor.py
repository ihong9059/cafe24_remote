
gatewayLocalServerIp = '127.0.0.1'
gatewayLocalServerPort = 5001

# cloudServerIp = '192.168.1.5'
cloudServerIp = '1.234.23.229'
# cloudServerIp = '0.0.0.0'
# cloudServerPort = 5001 
# cloudServerIp = '127.0.0.1' #for local test
cloudServerPort = 5002 #for local test

# cloudLocalIp = '127.0.0.1' #for local test
# cloudLocalPort = 5003 #for local test
finalReceiveIp = '127.0.0.1'
finalReceivePort = 5003


batteryIp = '127.0.0.1'
batteryPort = 12345

"""
(for test)generateLocalData.py: generate raw data from local

localDataSendServer.py: receive data from generateLocalData.py, 
    send data to cloudDataServer that is working inside of pybo.

cloudDataServer.py: receive data from localDataSendServer.py(local),
    send data to remoteReceiveData.py

(for test)remoteReceiveData.py: final destination. receive data from cloudDataServer.py,
    and display result.
"""