class ConfigurationService:
    def __init__(self, config_manager):
        self.config_manager = config_manager

    def get_configuration(self, key):
        # Logic to retrieve configuration settings
        return self.config_manager.get(key)

    def set_configuration(self, key, value):
        # Logic to update configuration settings
        self.config_manager.set(key, value)