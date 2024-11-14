#!/usr/bin/python3
"""imports JSON module"""
import json


def load_from_json_file(filename):
    """reads data from JSON file"""
    with open(filename, "r", encoding="utf-8") as a:
        data = json.load(a)
        return data
