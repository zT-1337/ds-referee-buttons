import json

class Config:
    config: None

    def __init__(self):
        self.load()
        pass

    def load(self):
        with open("config.json") as config_file:
            self.config = json.load(config_file)

    def get(self, key):
        return self.config[key]