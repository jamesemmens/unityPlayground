import socket
import argparse
import sys
import time


class Server:

    HOSTNAME = socket.gethostname()
    TCP_PORT = 25001
    DEST_IP = '127.0.0.1'
    ##MULTICAST_PORT = 55555
    LISTEN_HOST_PORT = (DEST_IP, TCP_PORT)

    READ_BUFFER = 2048
    BACKLOG = 10
    cube_location = '0,0,0'
    ENCODING = 'utf-8'

    TTL = 1
    #TTL_BYTE = struct.pack('B', TTL)

    def __init__(self):
        #self.thread_list = []
        #self.rooms = {} # {room_name: (multicast_address, multicast_port, message_history)}
        self.run()

    def run(self):
        try:
            self.connect_to_server()
            #self.initialize_listen_socket()

            self.send_to_server()
            #self.process_connections()
        except Exception as msg:
            print(msg)
            sys.exit(1)

    def connect_to_server(self):
        try:
            self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.connection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.connection.connect(self.LISTEN_HOST_PORT)
        except Exception as msg:
            print(msg)
            sys.exit(1)

    def send_to_server(self):
        try:
            for i in range(1,100):
                x = 0
                y = str(0.5*i)
                z = 0
                self.cube_location = str(x) + ',' + str(y) + ',' + str(z)
                print("\nCube location: ")
                print(self.cube_location)
                print("\nHost port: ")
                print(self.LISTEN_HOST_PORT)

                self.connection.sendall(self.cube_location.encode(Server.ENCODING))

                time.sleep(0.15)

        except Exception as msg:
            print(msg)
            sys.exit(1)



if __name__ == "__main__":
    roles = {
        'Server': Server
    }

    parser = argparse.ArgumentParser()

    parser.add_argument('-r', '--role',
                        choices=roles,
                        help='Client or Server role',
                        required=True,
                        type=str)

    args = parser.parse_args()

    roles[args.role]()
