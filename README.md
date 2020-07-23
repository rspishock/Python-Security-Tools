# Python-Security-Tools
A collection of security and pen testing tools written in Python

## Tools
### mac_changer.py
### network_scanner.py


##### Tools and technologies used
##### Environment
The script was originally created using PycharmCE on a Late 2018 MacBook Pro, 32GB RAM, 6 Core Intel i9, with 1TB SSD.


#### mac_changer.py
A simple script which can be used to alter the MAC address of Linux based systems.  The user is able to specify a MAC address for ease of recognition or have the script generate a random MAC address.

##### Imports
The following modules were used in this script:
- subprocess
  - This module is used to execute system level commands
- optparse
  - This module is used to parse arguments from the command line
- random
  - This module is used to generate random MAC addresses
- re
  - This module is used to parse the output of the if config command and extract the current MAC address for the interface.

##### Usage
python3 mac_changer.py -i --interface <value> -m --mac <value>



#### network_scanner.py
A simple script which can be used to send and receive ARP packets for host identification.

##### Imports
The following modules were used in this script:
- scapy
  - This module is used to manipulate data packets.

##### Usage
python3 network_scanner.py 