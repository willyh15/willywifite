import subprocess
import re

class NetworkScanService:
    def __init__(self, update_callback, interface):
        self.background_process = BackgroundProcess()
        self.update_callback = update_callback
        self.interface = interface

    def perform_scan(self):
        # Use the background_process to perform a scan in a non-blocking way
        self.background_process.run(self._actual_scanning_logic)

    def _actual_scanning_logic(self):
        # Use system command to perform scanning
        try:
            # Here iwlist is used for scanning, replace with your choice of tool or library
            scan_result = subprocess.check_output(["iwlist", self.interface, "scan"], text=True)
            networks = self._parse_scan_results(scan_result)
            self.update_callback(networks)
        except subprocess.CalledProcessError as e:
            print(f"An error occurred while scanning networks: {e}")
            self.update_callback([])

    def _parse_scan_results(self, scan_output):
        # A simple parser to extract network names (SSIDs) from the scan output
        pattern = re.compile(r'ESSID:"(.*?)"')
        ssids = pattern.findall(scan_output)
        networks = [{'name': ssid, 'signal': 'Unknown', 'security': 'Unknown'} for ssid in ssids]
        return networks
