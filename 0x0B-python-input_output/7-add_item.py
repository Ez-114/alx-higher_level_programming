#!/usr/bin/python3
"""7-add_item Module"""
import sys
import os

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

file_name = "add_item.json"

# load data from existing json file
if os.path.exists(file_name):
    items = load_from_json_file(file_name)
else:
    items = []

# add all command line args execluding the script name
items.extend(sys.argv[1:])

# store the updated list back to the json file
save_to_json_file(items, file_name)
