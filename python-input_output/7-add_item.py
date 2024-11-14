#!/usr/bin/python3
"""adds arguments to list and saves to file"""


from sys import argv
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
filename = "add_item.json"

try:
    # load data from file
    json_list = load_from_json_file(filename)
except FileNotFoundError:
    # initialize empty list if not found
    json_list = []

# append arguments to list
for arg in argv[1:]:
    json_list.append(arg)

# save updated list to file
save_to_json_file(json_list, filename)
