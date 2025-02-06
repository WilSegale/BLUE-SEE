from DontEdit import *

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
        
        # Scan the network for IP addresses
        scan_network("192.168.1.1/24")  # Change this to match your network
    else:
        print("Invalid choice. Please choose 1, 2, or 3.")

# Function to check Bluetooth status
def check_bluetooth_status():
    try:
        result = subprocess.run(['system_profiler', 'SPBluetoothDataType'], capture_output=True, text=True)
        if 'Bluetooth: Off' in result.stdout:
            print("Bluetooth is disabled")
        else:
            print("Bluetooth is enabled")
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to start the BlueSeeScan
def BlueSeeScan():
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
                await asyncio.sleep(5)  # Adjust scan interval

        try:
            asyncio.run(track_ble_devices())
        except KeyboardInterrupt:
            print("EXITING BLUE SEE")
    else:
        print("USE ROOT FOR THIS PROGRAM")

# Function to start BlueSEENetwork
def scan_network(ip_range):
    # Scan the network for IP addresses
    print("\n🔍 Scanning network for connected devices...")
    arp_request = scapy.ARP(pdst=ip_range)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=2, verbose=False)[0]

    for element in answered_list:
        print(f"🖥️  IP: {element[1].psrc}  |  MAC: {element[1].hwsrc}")
        print(f"🖥️  IP: {element[1].psrc}  |  MAC: {element[1].hwsrc}", file=BLUE_SEE_SCAN_IP)

# Allow the user to choose what function to run
user_choice()