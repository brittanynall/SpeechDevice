import socket
import json
from threading import Thread
import logging

debug_logger = logging.getLogger(__name__)

class NetworkService:
    LOCALHOST = ''
    SERVER_DISCOVERY_PORT = 9124
    BROADCAST_ADDR = '255.255.255.255'
    DISCOVERED_DEVICES = {}
    TCP_BUF_SIZE = 1024

    def _init__(self, callBack=None, HOST='', PORT=9124):
        self.HOST = HOST                            # localhost
        self.PORT = PORT                            # non-privileged port
        self.newDeviceCallBack = callBack

    def add_client(self, msg, addr):
        #if addr[0] not in networkService.DISCOVERED_DEVICES.keys():
        print (msg, addr)
        #    self.DISCOVERED_DEVICES[addr[0]] = addr[1]

    def get_devices(self):
        return self.DISCOVERED_DEVICES.keys()

    def start_service(self):
        network_discovery_listener = self.NetworkDiscoveryListener(self)
        network_disc_list_thread = Thread(target=network_discovery_listener.start_discovery_listener)
        network_disc_list_thread.start()

    class NetworkDiscoveryListener:
        def __init__(self, networkService):
            self.networkService = networkService

        def start_discovery_listener(self):
            udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            udpSocket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
            udpSocket.bind((NetworkService.LOCALHOST, NetworkService.SERVER_DISCOVERY_PORT))
            try:
                while True:
                    msg, addr = udpSocket.recvfrom(1024)
                    if self.networkService.isBroadcastPacket(msg.decode('utf-8')):
                        debug_logger.debug("Device discovered %s" % addr[0])
                        #networkService.add_client(msg, addr)
                        self.reply_discovery_msg(udpSocket, addr)
            finally:
                udpSocket.close()

        def reply_discovery_msg(self, connection, addr):
            ack = {'SERVICE':'ACD','TYPE':'BROADCAST','COMMAND':'ACK','DEV_NAME':'Speech Device - Test'}
            jsonAck = json.dumps(ack)
            connection.sendto(jsonAck.encode('utf-8'), addr)

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