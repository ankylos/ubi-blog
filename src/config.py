import sys
from os.path import abspath, join
from yaml import load, Loader

DEFAULT_CONFIG_FILEPATH = abspath(join(__file__, "../..", "ubi-blog.config.yaml"))

def read_config(config_filepath: str="") -> dict:
    if config_filepath == "":
        config_filepath = DEFAULT_CONFIG_FILEPATH

    try:
        with open(config_filepath, "r") as f:
            print(f"Loaded config file : {config_filepath}")
            return load(f, Loader=Loader)
    except Exception:
        print(f"Unable to find config in : {config_filepath}")
        sys.exit(1)
