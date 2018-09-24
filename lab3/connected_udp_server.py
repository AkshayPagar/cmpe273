from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor


class ConnectedUDPServer(DatagramProtocol):

    def datagramReceived(self, data, addr):
        print("received {} from {}".format(data.decode('utf-8'), addr))
        self.transport.write(data, addr)

reactor.listenUDP(1234,ConnectedUDPServer())
reactor.run()
