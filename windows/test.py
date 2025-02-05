import os
import asyncio
import subprocess
from bluetooth import discover_devices  # Requires `pybluez`
import pyfiglet

# Import all necessary functions from "DontEdit" (ensure this exists)
from DontEdit import *

# Banner Display
banner = pyfiglet.figlet_format("WIFI-SEE-SCAN")
print(banner)

# Function to allow the user to choose what to execute
def user_choice():
    print("Choose the function to execute:")
    print("1: Check Bluetooth status")
    print("2: Start BlueSeeScan")
    print("3: Start Mac_SEE")
    choice = input("Enter the number of your choice: ")

    if choice == "1":
        check_bluetooth_status()  # Call Bluetooth status check
    elif choice == "2":
        BlueSeeScan()  # Call BlueSeeScan
    elif choice == "3":
        scan_network()  # Scan the network for connected devices
    else:
        print("Invalid choice. Please choose 1, 2, or 3.")

# Function to check Bluetooth status on Windows
def check_bluetooth_status():
    try:
        result = subprocess.run("powershell Get-Service bthserv", capture_output=True, text=True, shell=True)
        if "Running" in result.stdout:
            print("✅ Bluetooth is enabled")
        else:
            print("❌ Bluetooth is disabled")
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to start the BlueSeeScan (Bluetooth scanning)
def BlueSeeScan():
    print("\n🔍 Scanning for Bluetooth devices...")
    
    try:
        devices = discover_devices(duration=8, lookup_names=True)
        for addr, name in devices:
            print(f"✅ Found: {name} [{addr}]")
    except Exception as e:
        print(f"⚠️ Bluetooth scan error: {e}")

# Function to scan the network on Windows
def scan_network():
    print("\n🔍 Scanning network for connected devices...\n")
    os.system("arp -a")  # Windows ARP scan (alternative to Scapy)

# Allow the user to choose what function to run
user_choice()
