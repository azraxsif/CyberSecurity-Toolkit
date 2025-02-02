# This program checks for specific protocols (e.g., TCP, UDP, ICMP, ARP) and extracts relevant information like source/destination IPs, ports, flags, and payloads.
from scapy.all import sniff, Ether, IP, TCP, UDP, ARP, ICMP
# scapy captures packets 
def packet_callback(packet):
    
    # callback function to process each captured packet.
 
    if Ether in packet:
        print("\n[+] Ethernet Frame:")
        print(f"Source MAC: {packet[Ether].src}")
        print(f"Destination MAC: {packet[Ether].dst}")
      # extracts the ethernet frame from the packet

    if IP in packet:
        print("\n[+] IP Packet:")
        print(f"Source IP: {packet[IP].src}")
        print(f"Destination IP: {packet[IP].dst}")
        print(f"Protocol: {packet[IP].proto}")
      # extracts the IP from the packet

        if TCP in packet:
            print("\n[+] TCP Segment:")
            print(f"Source Port: {packet[TCP].sport}")
            print(f"Destination Port: {packet[TCP].dport}")
            print(f"Flags: {packet[TCP].flags}")
            if packet[TCP].payload:
                print(f"Payload: {bytes(packet[TCP].payload)}")
              # extracts TCP from the packet (if it uses TCP)

        elif UDP in packet:
            print("\n[+] UDP Datagram:")
            print(f"Source Port: {packet[UDP].sport}")
            print(f"Destination Port: {packet[UDP].dport}")
            if packet[UDP].payload:
                print(f"Payload: {bytes(packet[UDP].payload)}")
              # else it extracts udp from the packet

        elif ICMP in packet:
            print("\n[+] ICMP Packet:")
            print(f"Type: {packet[ICMP].type}")
            print(f"Code: {packet[ICMP].code}")
            if packet[ICMP].payload:
                print(f"Payload: {bytes(packet[ICMP].payload)}")
              # else it extracts ICMP from the packet

    if ARP in packet:
        print("\n[+] ARP Packet:")
        print(f"Operation: {packet[ARP].op}")
        print(f"Sender MAC: {packet[ARP].hwsrc}")
        print(f"Sender IP: {packet[ARP].psrc}")
        print(f"Target MAC: {packet[ARP].hwdst}")
        print(f"Target IP: {packet[ARP].pdst}")
      # extracts ARP from the packet

    print("-" * 50)

def start_sniffing(interface=None, count=0):
  
    # Start sniffing packets on the specified interface.
   
    print(f"[*] Starting packet sniffer on interface {interface or 'default'}...")
    sniff(iface=interface, prn=packet_callback, count=count)
  # it takes an interface (iface) and a callback function (prn) to process each packet.

if __name__ == "__main__":
    # specify the network interface (e.g., 'eth0', 'wlan0', etc.)
    # leeave as None to use the default interface
    interface = None

    # Specify the number of packets to capture (0 for unlimited)
    packet_count = 0

    start_sniffing(interface=interface, count=packet_count)
