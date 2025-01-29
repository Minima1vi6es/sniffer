from scapy.all import sniff, IP, TCP, UDP

def packet_handler(packet):
    if IP in packet:
        log_data = f"Source: {packet[IP].src} → Destination: {packet[IP].dst}"

        if TCP in packet:
            log_data += f" | TCP {packet[TCP].sport} → {packet[TCP].dport}"
        elif UDP in packet:
            log_data += f" | UDP {packet[UDP].sport} → {packet[UDP].dport}"
        else:
            log_data += f" | Other Protocol"

        print(log_data)

# Start sniffing
sniff(prn=packet_handler, store=False)
