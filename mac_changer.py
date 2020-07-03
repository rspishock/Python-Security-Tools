#!/usr/bin/env python3

import subprocess
import optparse
import random

def generate_mac():
  """Generates a random MAC address"""

  mac = ':'.join(("%012x" % random.randint(0, 0xFFFFFFFFFFFF))[i:i+2] for i in range(0, 12, 2))
  return mac


def change_mac(interface, mac):
  """Change MAC address for user specified interface."""
  print(f'[+] Changeing MAC address for interface {interface} to {mac}\n')
  # interface down
  subprocess.call(['ifconfig', interface, 'down'])

   # change MAC
  subprocess.call(['ifconfig', interface, 'hw', 'ether', mac])

  # interface up
  subprocess.call(['ifconfig', interface, 'up'])

  # verifies new MAC
  subprocess.call(['ifconfig', interface])


def get_arguements():
  """Get user supplied arguements from terminal."""

  parser = optparse.OptionParser()
  # arguements
  parser.add_option('-i', '--interface', dest='interface', help='Interface to change MAC address')
  parser.add_option('-m', '--mac', dest='mac', help='Specify new MAC address. Type "random" for random MAC.')

  (options, arguements) = parser.parse_args()

  # add call to random_mac
  if options.mac == 'random':
    generate_mac()

  if not options.interface :
    parser.error('[-] Please specify an interface, use --help for more info.')
  elif not options.mac:
    parser.error('[-] Please specify a new MAC, use --help for more info.')

  return options

options = get_arguements()
change_mac(options.interface, options.mac)
