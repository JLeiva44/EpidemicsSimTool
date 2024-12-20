import json

class SettingsLoader:
    '''Class for load configurations from JSON o YAML files'''
    @staticmethod
    def load_from_file(filepath):
        with open(filepath, 'r') as f:
            return json.load(f)
