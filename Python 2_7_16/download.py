#! /usr/bin/python
"""A simple script used to download files to the target system.
   Uses Python 2.7.16"""

import optparse
import requests


def get_arguments():
    """Get user supplied arguments from terminal."""
    parser = optparse.OptionParser()
    # arguments
    parser.add_option('-t', '--target', dest='target', help='File to obtain from the Internet.')

    (options, arguments) = parser.parse_args()

    return options


def download(url):
    """Obtains a document from the Internet to use as a trojan carrier file."""
    get_response = requests.get(url)

    file_name = url.split('/')[-1]

    with open(file_name, 'wb') as out_file:
        """Writes output to file on local disk"""
        out_file.write(get_response.content)
    

options = get_arguments()
download(options.target)
