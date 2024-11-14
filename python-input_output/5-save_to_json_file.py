#!/usr/bin/python3
"""imports required modules"""
import json


def save_to_json_file(my_obj, filename):
    """saves object to JSON file"""
    with open(filename, "w", encoding="utf-8") as a:
        json.dump(my_obj, a)
