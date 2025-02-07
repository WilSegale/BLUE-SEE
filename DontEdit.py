from bleak import BleakScanner
import asyncio
import pyfiglet
import scapy.all as scapy  # For network scanning
import os
import subprocess
# Open the output files
BLUE_SEE_SCAN_ON = open("BLUE_SEE_SCAN_ON.log", "w")
BLUE_SEE_SCAN_OFF = open("BLUE_SEE_SCAN_OFF.log", "w") 
BLUE_SEE_SCAN_IP = open("BLUE_SEE_SCAN_IP.log", "w")

# Print the banner
banner = pyfiglet.figlet_format("BLUE-SEE")