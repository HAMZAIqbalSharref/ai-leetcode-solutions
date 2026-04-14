import os

CONFIG_FILE = "config.txt"


def save_config(openai_key, github_token):
    with open(CONFIG_FILE, "w") as f:
        f.write(f"OPENAI_API_KEY={openai_key}\n")
        f.write(f"GITHUB_TOKEN={github_token}\n")


def load_config():
    if not os.path.exists(CONFIG_FILE):
        return None, None

    with open(CONFIG_FILE, "r") as f:
        lines = f.readlines()

    config = {}
    for line in lines:
        key, value = line.strip().split("=")
        config[key] = value

    return config.get("OPENAI_API_KEY"), config.get("GITHUB_TOKEN")