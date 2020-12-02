import json
import re


with open('../fields.json', 'r') as file:
	fields_json = json.load(file)

with open('../readme.txt', 'r') as file:
    readme_file = file.read()

# The following is an example of capturing the name field. Note I have not separated the readme into sections but in this instance it does not matter.
print("Searching readme for text matching pattern: ", fields_json['title']['name']['field_regex'])
pattern = fields_json['title']['name']['field_regex']
title = re.findall(pattern, readme_file, flags=re.MULTILINE)[fields_json['title']['name']['match']]

print(title)

# This example looks for the version in the readme.
print("Searching readme for text matching pattern: ", fields_json['title']['version']['field_regex'])
pattern = fields_json['title']['version']['field_regex']
version = re.findall(pattern, readme_file, flags=re.MULTILINE)[fields_json['title']['version']['match']]

print(version)

# This example looks for the author in the readme. Note I have not separated the readme into sections but in this instance it does not matter. I've also assigned a variable to the section's key to avoid retyping the very long dictionary index. This regex used a capture group but re manages it without any additional parameters.
section = fields_json['authorship']['author']
pattern = section['field_regex']
print("Searching readme for text matching pattern: ", pattern)
author = re.findall(pattern, readme_file, flags=re.MULTILINE)[section['match']]

print(author)
