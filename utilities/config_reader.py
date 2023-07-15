"""Reads the config"""
from configparser import ConfigParser


def read_configuration(category, key):
    """Returns the key for the given category"""
    config = ConfigParser()
    config.read("configurations/config.ini")
    return config.get(category, key)
