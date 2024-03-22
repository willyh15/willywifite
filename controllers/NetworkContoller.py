class NetworkController:
    def __init__(self, scanner_service):
        self.scanner_service = scanner_service

    def perform_scan(self):
        # Logic to start a network scan
        results = self.scanner_service.scan_networks()
        # Post-processing if needed
        return results