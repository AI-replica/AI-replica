import yaml


def read_config():
    with open("config.yaml") as file:
        try:
            return yaml.safe_load(file)
        except yaml.YAMLError as error:
            print(error)
            return {}


config = read_config()
