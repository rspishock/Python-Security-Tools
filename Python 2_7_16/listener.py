#! /usr/bin/python
"""A simple listener script.
   Uses Python 2.7.16"""

import optparse
import socket


def get_arguments():
    """Get user supplied arguments from terminal."""
    parser = optparse.OptionParser()
    # arguments
    parser.add_option('-l', '--local', dest='local_io', help='Attacking host IP.')
    parser.add_option('-p', '--port', dest='port', help='Port to connect to.')

    (options, arguments) = parser.parse_args()

    return options


options = get_arguments()

listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listener.bind((options.local_ip, options.port))
listener.listen()
