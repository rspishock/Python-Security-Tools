#!/usr/bin/env python3
"""A simple script used to scan a network for valid host/hosts.
Script uses Python 3"""

import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)                                                # sets destination IP address
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")                                # sets broadcast MAC address
    arp_request_broadcast = broadcast/arp_request                                   # creates ARP request
    answered_list, unanswered_list = scapy.srp(arp_request_broadcast, timeout=1)    # send/receive ARP packets
    print(answered_list.summary())


scan("192.168.1.1")
