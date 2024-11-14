#!/usr/bin/python3
"""imports JSON module"""
import json


def from_json_string(my_str):
    """converts JSON string to object"""
    return json.loads(my_str)
