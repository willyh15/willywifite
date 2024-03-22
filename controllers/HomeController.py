# controllers/home_controller.py

from services.network_scan_service import NetworkScanService
from services.attack_history_service import AttackHistoryService
from services.configuration_service import ConfigurationService

class HomeController:
    def __init__(self, network_scan_service, attack_history_service, configuration_service):
        self.network_scan_service = network_scan_service
        self.attack_history_service = attack_history_service
        self.configuration_service = configuration_service

    def start_scan(self):
        # Use the network_scan_service to start scanning
        self.network_scan_service.scan_for_networks()

    def get_attack_history(self):
        # Use the attack_history_service to get the history
        return self.attack_history_service.get_attack_history()

    def get_configuration(self, key):
        # Use the configuration_service to get the config
        return self.configuration_service.get_configuration(key)

    def set_configuration(self, key, value):
        # Use the configuration_service to update the config
        self.configuration_service.set_configuration(key, value)
