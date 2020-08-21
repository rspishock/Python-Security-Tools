#!/usr/bin/python
"""A simple script used to alter a systems MAC address.  User provides the interface, and can supply a MAC address or
   choose to use a randomly generated one.  Script uses Python 2.7.16"""

import subprocess
import optparse
import random
import re


def generate_mac():
    """Generates a random MAC address"""
    mac = ':'.join(("%012x" % random.randint(0, 0xFFFFFFFFFFFF))[i:i+2] for i in range(0, 12, 2))
    return mac


def get_arguments():
    """Get user supplied arguments from terminal."""
    parser = optparse.OptionParser()
    # arguments
    parser.add_option('-i', '--interface', dest='interface', help='Interface to change MAC address')
    parser.add_option('-m', '--mac', dest='new_mac', help='Specify new MAC address. Type "random" for random MAC.')

    (options, arguments) = parser.parse_args()

    # add call to random_mac
    if options.mac == 'random':
        options.mac = generate_mac()

    if not options.interface:
        parser.error('[-] Please specify an interface, use --help for more info.')
    elif not options.new_mac:
        parser.error('[-] Please specify a new MAC, use --help for more info.')

    return options


def change_mac(interface, new_mac):
    """Change MAC address for user specified interface."""
    print('[+] Changing MAC address for interface ' + interface + 'to ' + new_mac)
    # interface down
    subprocess.call(['ifconfig', interface, 'down'])

    # change MAC
    subprocess.call(['ifconfig', interface, 'hw', 'ether', new_mac])

    # interface up
    subprocess.call(['ifconfig', interface, 'up'])

    # # verifies new MAC
    # subprocess.call(['ifconfig', interface])


def get_current_mac(interface):
    """Returns current MAC address, if available."""
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_address_search_result = re.search(r"([0-9A-F]{2}[:-]){5}([0-9A-F]{2})", ifconfig_result.decode(), re.IGNORECASE)

    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print('[-] Could not read MAC address.')


options = get_arguments()
current_mac = get_current_mac(options.interface)    # gets original MAC address
print('Current MAC: ' + str(current_mac))

change_mac(options.interface, options.mac)          # changes MAC address

current_mac = get_current_mac(options.interface)    # gets MAC address after change
if current_mac == options.mac:
    print('[+] MAC address was successfully changed to ' + current_mac)
else:
    print('[-] MAC address was not changed')
