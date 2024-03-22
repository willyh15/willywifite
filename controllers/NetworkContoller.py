class NetworkController:
    def __init__(self, scanner_service):
        self.scanner_service = scanner_service

    def perform_scan(self):
        results = self.scanner_service.scan_for_networks()
        return results
