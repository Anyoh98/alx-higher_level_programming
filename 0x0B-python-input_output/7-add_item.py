#!/usr/bin/python3
import sys
"""Add all arguments to a Python list and save them to a file."""


# Dynamically import the functions using __import__
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

# Start from the second argument (index 1)
arguments = sys.argv[1:]

# Load the existing list or create an empty one
try:
    existing_list = load_from_json_file("add_item.json")
except FileNotFoundError:
    existing_list = []

# Create an empty list to store the arguments
my_list = []

# Add each argument to the list
for arg in arguments:
    my_list.append(arg)

# Combine the existing list and the new list
combined_list = existing_list + my_list

# Save the combined list to the JSON file
save_to_json_file(combined_list, "add_item.json")
