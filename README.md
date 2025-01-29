# 📡 Packet Sniffer

A simple Python-based **packet sniffer** that captures network traffic in real-time and logs details like **source/destination IPs, ports, and protocols**.

## 🛠 Features
- Captures real-time **network packets**.
- Supports **TCP, UDP, and other protocols**.
- Logs **source & destination IP addresses**.
- Lightweight and easy to use.

---

## 🚀 Installation

### 1️⃣ Install Dependencies
This script requires `scapy`. Install it using:

```bash
pip install scapy

----
## Usage

Run the script with administrator/root privileges:
sudo python3 sniffer.py

On Windows (run as administrator):
python sniffer.py
Packets will be captured and displayed in the terminal.

---

## Example Output

Example Output

[+] Packet Captured: IP 192.168.1.5 → 8.8.8.8
    Source IP: 192.168.1.5 → Destination IP: 8.8.8.8
    Protocol: TCP | Source Port: 55678 | Destination Port: 443

---

## Customizing

Customizing

To filter only TCP packets, modify:

sniff(prn=packet_handler, filter="tcp", store=False)

To log packets to a file, modify:

with open("packets.log", "a") as log_file:
    log_file.write(log_data + "\n")

---

## License

This project is licensed under the MIT License – feel free to use and modify it.
