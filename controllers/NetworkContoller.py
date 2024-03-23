from services.network_scan_service import NetworkScanService

class NetworkController:
    def __init__(self):
        self.network_scan_service = NetworkScanService()
        
    def scan_networks(self):
        # Use the network_scan_service to scan networks
        return self.network_scan_service.perform_scan()