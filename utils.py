import yaml



def get_config():
    with open("config.yaml", "r") as f:
        config = yaml.safe_load(f)
    env = config["env"]
    return config[env]
