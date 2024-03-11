import sys
from os.path import abspath, join

import tomli

DEFAULT_CONFIG_FILEPATH = abspath(join(__file__, "../..", "ubi-blog.config.toml"))

def read_config(config_filepath: str="") -> dict:
    if config_filepath == "":
        config_filepath = DEFAULT_CONFIG_FILEPATH

    try:
        with open(config_filepath, mode="rb") as f:
            print(f"Loaded config file : {config_filepath}")
            return tomli.load(f)
    except Exception as exc:
        print(f"Unable to find config in : {config_filepath}")
        raise exc
