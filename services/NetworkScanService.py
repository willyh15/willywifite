# services/network_scan_service.py
from utils.background import BackgroundProcess

class NetworkScanService:
    def __init__(self):
        self.background_process = BackgroundProcess()

    def perform_scan(self):
        # Use the background_process to perform a scan in a non-blocking way
        self.background_process.run(self._actual_scanning_logic)

    def _actual_scanning_logic(self):
        # Actual scanning logic goes here
        pass