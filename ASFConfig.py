import json


class ASFConfig:
    asf_config = None
    path = None

    def __init__(self, path):
        self.path = path
        with open(path) as f:
            self.asf_config = json.load(f)

    def get_GamesPlayedWhileIdle(self):
        return self.asf_config['GamesPlayedWhileIdle']

    def print_current_config(self):
        print(self.asf_config)

    def update_GamesPlayedWhileIdle(self, appid_list):
        self.asf_config['GamesPlayedWhileIdle'] = appid_list
        self.write_to_asf_config_file()

    def write_to_asf_config_file(self):
        print("Updating ASF config files ...")
        with open(self.path, 'w') as outfile:
            json.dump(self.asf_config, outfile, sort_keys=True, indent=4)