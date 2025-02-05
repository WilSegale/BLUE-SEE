import asyncio
from bleak import BleakScanner
import pyfiglet
import scapy.all as scapy  # For network scanning
import os

BLUE_SEE_SCAN_ON = open("BLUE_SEE_SCAN_ON.txt", "w")
BLUE_SEE_SCAN_OFF = open("BLUE_SEE_SCAN_OFF.txt", "w") 
BLUE_SEE_SCAN_IP = open("BLUE_SEE_SCAN_IP.txt","w")
banner = pyfiglet.figlet_format("BLUE-SEE-SCAN")
print(banner)

if os.geteuid() == 0:
    async def track_ble_devices():
        print("Tracking active BLE devices... Press Ctrl+C to stop.")
        active_devices = {}  # Store active devices {address: name}

        while True:
            devices = await BleakScanner.discover()
            current_devices = {device.address: device.name for device in devices if device.name}

            # Check for new devices
            for addr, name in current_devices.items():
                if addr not in active_devices:
                    print(f"✅ Found: {name} [{addr}]")
                    print(f"✅ Found: {name} [{addr}]", file=BLUE_SEE_SCAN_ON)
            
            # Check for devices that disappeared
            for addr in list(active_devices.keys()):
                if addr not in current_devices:
                    print(f"❌ This device is turned off: {active_devices[addr]} [{addr}]")
                    print(f"❌ This device is turned off: {active_devices[addr]} [{addr}]", file=BLUE_SEE_SCAN_OFF)
                    del active_devices[addr]

            active_devices = current_devices  # Update active devices list

            # Scan the network for IP addresses
            scan_network("192.168.1.1/24")  # Change this to match your network

            await asyncio.sleep(5)  # Adjust scan interval

    def scan_network(ip_range):
        print("\n🔍 Scanning network for connected devices...")
        arp_request = scapy.ARP(pdst=ip_range)
        broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        arp_request_broadcast = broadcast / arp_request
        answered_list = scapy.srp(arp_request_broadcast, timeout=2, verbose=False)[0]

        for element in answered_list:
            print(f"🖥️  IP: {element[1].psrc}  |  MAC: {element[1].hwsrc}")
            print(f"🖥️  IP: {element[1].psrc}  |  MAC: {element[1].hwsrc}",file=BLUE_SEE_SCAN_IP)

    try:
        asyncio.run(track_ble_devices())
    except KeyboardInterrupt:
        print("EXITING BLUE SEE")
else:
    print("USE ROOT FOR THIS PORGRAM")