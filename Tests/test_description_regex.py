import json
import re

JSON_FILE = None

def setup_module(module):
	with open('../fields.json', 'r') as file:
		global JSON_FILE
		file = json.load(file)
		JSON_FILE = file['description']

'''
Description Section
'''
def test_long_description():
	regex = re.compile(JSON_FILE['long_description']['regex'], re.M)
	test_list = ["Description\n\n"
				 "A basic parser to extract setup.py metadata fields from a NKMF-compliant (and UEWSG-compliant!) UTF-8 readme file."]
	matches = []
	for test in test_list:
		match = regex.match(test)
		if match is not None:
			matches.append(match.group(1))
	test_answers = ["A basic parser to extract setup.py metadata fields from a NKMF-compliant (and UEWSG-compliant!) UTF-8 readme file."]
	assert matches == test_answers, "DESC. LONG - returns wrong string."

def test_long_description_content_type():
	assert JSON_FILE['long_description_content_type'] == 'text/plain', "DESC. CONTENT TYPE - returns wrong string."
