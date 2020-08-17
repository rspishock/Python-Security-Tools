# Python-Security-Tools
A collection of security and pen testing tools written in Python3

## Tools
### - mac_changer.py
### - network_scanner.py
### - arp_spoof.py
### - packet_sniffer.py
### - net_cut.py
### - dns_spoof.py
### - replace_downloads.py
### - code_injector.py
### - arpspoof_detector.py


## Tools and technologies used
#### Environment
The script was originally created using PycharmCE on a Late 2018 MacBook Pro, 32GB RAM, 6 Core Intel i9, with 1TB SSD.


## Scripts

### mac_changer.py
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
python3 mac_changer.py -i --interface <value>


### net_cut.py


#### Imports
The following modules were used in this script:
- netfilterqueue
  - This module is used to 
- scapy.all
  - This module is used to sniff the network for packets.

##### Usage
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
python3 code_injector.py -i --ip <attacking IP> -p --port <port number>


### arpspoof_detector.py
A simple script used to detect the presence of an ARP spoofing attack.

#### Imports
The following modules were used in this script:
- scapy.all
  - This module is used to sniff the network for packets.

##### Usage
python3 arpspoof_detector.py