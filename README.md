# Python-Security-Tools (WIP)
__*All scripts are currently untested*__

A collection of security and pen testing tools and malware written in Python.

I have included versions of the scripts in both Python 2.7.16 and 3.8.0.

While Python 2.x has reached end of life, scripts are being included for backwards compatibility in the event that Python 3.x is not available on target machine.

## Tools
#### - mac_changer.py
#### - network_scanner.py
#### - arp_spoof.py
#### - packet_sniffer.py
#### - net_cut.py
#### - dns_spoof.py
#### - replace_downloads.py
#### - code_injector.py
#### - arpspoof_detector.py
#### - download_execute_and_report.py
#### - keylogger.py
#### - spider.py


## Tools and technologies used
#### Coding environment
##### Hardware
- Late 2018 MacBook Pro
    - 32GB RAM
    - 6 Core Intel i9 processor
    - 1TB SSD

##### Software
- MacOS Catalina
- PycharmCE
- Kite

##### Github repo
- https://github.com/rspishock/Python-Security-Tools

## Scripts

### mac_changer.py
##### Python 2.7.x - Tested/Approved
A simple script which can be used to alter the MAC address of Linux based systems.  The user is able to specify a MAC address for ease of recognition or have the script generate a random MAC address.

#### Imports
The following modules were used in this script:
- subprocess
  - This module is used to execute system level commands
- argparse
  - This module is used to parse arguments from the command line
- random
  - This module is used to generate random MAC addresses
- re
  - This module is used to parse the output of the if config command and extract the current MAC address for the interface.

##### Usage
__Python 2.7.x__
python mac_changer.py -i --interface <value> -m --mac <value>

__Python 3__
python3 mac_changer.py -i --interface <value> -m --mac <value>



### network_scanner.py
A simple script which can be used to send and receive ARP packets for host identification.  Script will return target IPs and MAC addresses.

#### Imports
The following modules were used in this script:
- scapy
  - This module is used to manipulate data packets.
  - __Must be installed on Python3__
    - pip3 install scapy-python3
  
- argparse
  - This module is used to parse arguments from the command line

##### Usage
__Python 2.7.x
python network_scanner.py -t --target <ip address/range>

__Python 3__
python3 network_scanner.py -t --target <ip address/range>


### arp_spoof.py
A simple script which can be used to initialize a MiTM attack.

#### Imports
The following modules were used in this script:
- scapy
  - This module is used to manipulate data packets.
  - __Must be installed on Python3__
    - pip3 install scapy-python3
- argparse
  - This module is used to parse arguments from the command line
- time
  - This module is used to control the delay in resending spoof packets

##### Usage
__Python 2.7.x__
python arp_spoof.py

__Python 3__
python3 arp_spoof.py 

### packet_sniffer.py
A simple script used to sniff packets coming across the network and extract data.

#### Imports
The following modules were used in this script:
- scapy.layers
  - This module is used to search packets for specified layers
- scapy.all
  - This module is used to sniff the network for packets.
- argparse
  - This module is used to parse arguments from the command line

##### Usage
__Python 2.7.x__
python3 mac_changer.py -i --interface <value>

__Python 3__
python3 mac_changer.py -i --interface <value>


### net_cut.py


#### Imports
The following modules were used in this script:
- netfilterqueue
  - This module is used to 
- scapy.all
  - This module is used to sniff the network for packets.

##### Usage
__Python 2.7.x__
python net_cut.py

__Python 3__
python3 net_cut.py


### dns_spoof.py
A simple script used to intercept and spoof DNS packets.

#### Imports
The following modules were used in this script:
- netfilterqueue
  - This module is used to 
- scapy.all
  - This module is used to sniff the network for packets.
 - argparse
  - This module is used to parse arguments from the command line

##### Usage
__Python 2.7.x__
python mac_changer.py

__Python 3__
python3 mac_changer.py


### replace_download.py
A simple script used to intercept download requests and replace the good payload with malicious payloads.

#### Imports
The following modules were used in this script:
- netfilterqueue
  - This module is used to 
- scapy.all
  - This module is used to sniff the network for packets.
 - argparse
  - This module is used to parse arguments from the command line

##### Usage
__Python 2.7.x__
python replace_download.py

__Python 3__
python3 replace_download.py


### code_injector.py
A simple script used to inject code into.

#### Imports
The following modules were used in this script:
- netfilterqueue
  - This module is used to 
- argparse
  - This module is used to parse arguments from the command line
- scapy.all
  - This module is used to sniff the network for packets.
- re
  - This module is used to create regular expressions

##### Usage
python3 code_injector.py -i --ip (attacking IP) -p --port (port number)


### arpspoof_detector.py
A simple script used to detect the presence of an ARP spoofing attack.

#### Imports
The following modules were used in this script:
- scapy.all
  - This module is used to sniff the network for packets.

##### Usage
__Python 2.7.x__
python arpsoff_detector.py

__Python 3__
python3 arpspoof_detector.py


### execute_command.py
A simple script used to extract wifi settings from a target host.

#### Imports
The following modules were used in this script:
- subprocess
- optparse
    - This module is used to parse arguments from the command line
- argparse __*Python 3 only*__
    - This module is used to parse arguments from the command line
- smtplib
    - This module is used to send emails from Python script

##### Usage
__Python 2.7.x__
python execute_command.py -e --email (email address to send output to) -p --password (email password)

__Python 3__
python3 execute_command.py -e --email (email address to send output to) -p --password (email password)


### download.py
A simple script used to download files to the target system.

#### Imports
The following modules were used in this script:
- requests
    - This module allows the script to send requests to the Internet.
- optparse
    - This module is used to parse arguments from the command line
- argparse __*Python 3 only*__
    - This module is used to parse arguments from the command line

##### Usage
__Python 2.7.x__
python download.py -t --target (target URL)

__Python 3__
python3 download.py -t --target (target URL)


# NEEDS UPDATED BELOW


### download_execute_and_report.py
A simple script used to extract passwords from a target host.

#### Imports
The following modules were used in this script:
- subprocess
- optparse
- requests
- tempfile
- smtplib
- os

##### Usage
__Python 2.7.x__
python 

__Python 3__
python3 


### keylogger.py
A simple keylogger class.

#### Imports
The following modules were used in this script:
- pynput
    - This module allows the script to monitor for keyboard and mouse activity.
- threading
    - This module 
- smtplib
    - 

##### Usage
__Python 2.7.x__
python keylogger.py

__Python 3__
python3 keylogger.py


### reverse_backdoor.py
A simple backdoor script.

#### Imports
The following modules were used in this script:
- socket
- optparse
- subprocess

##### Usage
__Python 2.7.x__
python keylogger.py

__Python 3__
python3 keylogger.py



### listener.py
A simple listener script.

#### Imports
The following modules were used in this script:
- socket
- optparse

##### Usage
__Python 2.7.x__
python keylogger.py

__Python 3__
python3 keylogger.py


### execute_command.py
A simple script to crawl a URL checking for all available links.

#### Imports
The following modules were used in this script:
- requests
- optparse
- urlparse
- re

##### Usage
__Python 2.7.x__
python spider.py -t --target (target URL)

__Python 3__
python3 spider.py -t --target (target URL)
