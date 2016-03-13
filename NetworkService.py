import socket
import json
from threading import Thread

class NetworkService:
    LOCALHOST = ''
    SERVER_DISCOVERY_PORT = 9124
    SERVER_PORT = 9125
    BROADCAST_ADDR = '255.255.255.255'
    ACD_CLIENT_MSG = b'ACD_DEVICE_DISCOVERY'
    ACD_SERVER_MSG = b'ACD_SERVER:PORT:'
    DISCOVERED_DEVICES = {}
    TCP_BUF_SIZE = 1024

    def _init__(self, HOST='', PORT=9124):
        self.HOST = HOST                            # localhost
        self.PORT = PORT                            # non-privileged port

    def add_client(self, msg, addr):
        #if addr[0] not in networkService.DISCOVERED_DEVICES.keys():
        print (msg, addr)
        #    self.DISCOVERED_DEVICES[addr[0]] = addr[1]

    def get_devices(self):
        return self.DISCOVERED_DEVICES.keys()

    def start_service(self):
        #network_server = self.NetworkServer(self)
        network_discovery_listener = self.NetworkDiscoveryListener(self)

        #network_server_thread = Thread(target=network_server.start_server)
        network_disc_list_thread = Thread(target=network_discovery_listener.start_discovery_listener)

        #network_server_thread.start()
        network_disc_list_thread.start()

    class NetworkDiscoveryListener:
        def __init__(self, networkService):
            self.networkService = networkService

        def start_discovery_listener(self):
            """
            Starts a thread and listens to clients trying to connect to the devices.
            :return:
            """
            udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            udpSocket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
            udpSocket.bind((NetworkService.LOCALHOST, NetworkService.SERVER_DISCOVERY_PORT))
            try:
                while True:
                    msg, addr = udpSocket.recvfrom(1024)
                    if self.networkService.isBroadcastPacket(msg.decode('utf-8')):
                        networkService.add_client(msg, addr)
                        self.reply_discovery_msg(udpSocket, addr)
            finally:
                udpSocket.close()

        def reply_discovery_msg(self, connection, addr):
            ack = {'SERVICE':'ACD','TYPE':'BROADCAST','COMMAND':'ACK'}
            jsonAck = json.dumps(ack)
            connection.sendto(jsonAck.encode('utf-8'), addr)

    class NetworkServer:
        def __init__(self, networkService):
            self.networkService = networkService

        def start_server(self):
            tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                tcp_socket.bind((networkService.LOCALHOST, networkService.SERVER_PORT))
                tcp_socket.listen(1)
                while True:
                    connection, addr = tcp_socket.accept()
                    data = connection.recv(networkService.TCP_BUF_SIZE)
                    if data:
                        connection.send(data)
                    connection.close()
            finally:
                tcp_socket.close()

    def isBroadcastPacket(self, jsonPacket):
        data = json.loads(jsonPacket)
        try:
            if data['SERVICE'] == 'ACD' \
                    and data['TYPE'] == 'BROADCAST' \
                    and data['COMMAND'] == 'REQUEST':
                return True
        except KeyError or TypeError as e:
            print(e)
            pass

        return False



if __name__ == '__main__':
    networkService = NetworkService()
    networkService.start_service()
    while True: pass