import asyncio
from bleak import *

try:
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
            
            # Check for devices that disappeared
            for addr in list(active_devices.keys()):
                if addr not in current_devices:
                    print(f"❌ This device is turned off: {active_devices[addr]} [{addr}]")
                    del active_devices[addr]

            active_devices = current_devices  # Update active devices list

            await asyncio.sleep(5)  # Adjust scan interval as needed

    asyncio.run(track_ble_devices())
except KeyboardInterrupt:
    print("EXITING BLUE SEE")