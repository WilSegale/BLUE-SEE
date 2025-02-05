# BLUE-SEE-SCAN

**BLUE-SEE-SCAN** is a Python script designed to scan for nearby Bluetooth devices (BLE) and track active devices, checking if they are turned on or off. Additionally, it scans the local network for connected devices (IP and MAC addresses) using ARP requests.

## Features

- **Bluetooth Scanning**: The script scans for nearby Bluetooth Low Energy (BLE) devices and displays their names and MAC addresses.
- **Device Tracking**: Tracks devices that are on or off, with notifications when a device is found or turned off.
- **Network Scanning**: Scans the local network for connected devices (IP addresses and MAC addresses).
- **Text Output**: Results are written to text files for further analysis (`BLUE_SEE_SCAN_ON.txt`, `BLUE_SEE_SCAN_OFF.txt`, `BLUE_SEE_SCAN_IP.txt`).
- **ASCII Banner**: A banner is displayed using `pyfiglet`.

## Requirements

To run this script, you need the following Python packages:

- `bleak`: For scanning Bluetooth devices.
- `pyfiglet`: For generating an ASCII banner.
- `scapy`: For network scanning (ARP requests).

### Install Dependencies

To install the required dependencies, run:

```sh
pip3 install -r requirements.txt