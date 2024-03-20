import json

class Configuration:
    def __init__(self, config_file='config.json'):
        self.config_file = config_file
        self.settings = self.load_config()

    def load_config(self):
        try:
            with open(self.config_file, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}  # Return an empty config if none exists

    def save_config(self):
        with open(self.config_file, 'w') as file:
            json.dump(self.settings, file, indent=4)

    def get_setting(self, key, default=None):
        return self.settings.get(key, default)

    def update_setting(self, key, value):
        self.settings[key] = value
        self.save_config()
