from scapy.all import *
import scapy.all as scapy
import time

target_ip = "FF.FF.FF.1/24"

# Open output file
with open("suspicious_traffic.txt", "a") as f:
    # Start an infinite loop
    while True:
        def detect_packet(pkt):
            if pkt.haslayer(scapy.TCP) and pkt.haslayer(Raw) and b"MS_T120" in pkt[Raw].load:
                print("[+] Remote Desktop connection detected from " + pkt[scapy.IP].src + ":" + str(pkt[scapy.TCP].sport))
                f.write("[+] Remote Desktop connection detected from " + pkt[scapy.IP].src + ":" + str(pkt[scapy.TCP].sport) + "\n")
            elif pkt.haslayer(scapy.ICMP) and pkt.getlayer(scapy.ICMP).type == 8:
                print("[+] Ping detected from " + pkt[scapy.IP].src)
                f.write("[+] Ping detected from " + pkt[scapy.IP].src + "\n")
            elif pkt.haslayer(scapy.TCP) and pkt.getlayer(scapy.TCP).flags == "S":
                print("[+] SYN packet detected from " + pkt[scapy.IP].src + ":" + str(pkt[scapy.TCP].sport))
                f.write("[+] SYN packet detected from " + pkt[scapy.IP].src + ":" + str(pkt[scapy.TCP].sport) + "\n")
            elif pkt.haslayer(scapy.IP) and pkt.haslayer(scapy.TCP) and pkt[scapy.IP].dst == "ATTACKER_IP_ADDRESS_OR_DOMAIN":
                print("[+] Outbound connection detected to attacker from " + pkt[scapy.IP].src + ":" + str(pkt[scapy.TCP].sport))
                f.write("[+] Outbound connection detected to attacker from " + pkt[scapy.IP].src + ":" + str(pkt[scapy.TCP].sport) + "\n")
            elif pkt.haslayer(scapy.DNS) and len(pkt[scapy.DNSQR].qname) > 50:
                print("[+] Possible DNS tunneling detected from " + pkt[scapy.IP].src + " to " + pkt[scapy.DNSQR].qname.decode())
                f.write("[+] Possible DNS tunneling detected from " + pkt[scapy.IP].src + " to " + pkt[scapy.DNSQR].qname.decode() + "\n")
            elif pkt.haslayer(scapy.ARP) and pkt[scapy.ARP].op == 2:
                print("[+] Possible ARP spoofing detected from " + pkt[scapy.IP].src + " to " + pkt[scapy.ARP].psrc)
                f.write("[+] Possible ARP spoofing detected from " + pkt[scapy.IP].src + " to " + pkt[scapy.ARP].psrc + "\n")
            elif pkt.haslayer(scapy.TCP) and pkt.haslayer(Raw) and (b"USER" in pkt[Raw].load or b"PASS" in pkt[Raw].load):
                print("[+] FTP command detected from " + pkt[scapy.IP].src + ": " + pkt[Raw].load.decode().strip())
                f.write("[+] Possible FTP command detected from " + pkt[scapy.IP].src + "\n")

        sniff(filter="tcp or icmp or udp or arp", prn=detect_packet, store=0)
