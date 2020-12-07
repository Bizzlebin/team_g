import json
import re

JSON_FILE = None

def setup_module(module):
	with open('../fields.json', 'r', encoding = 'UTF-8') as file:
		global JSON_FILE
		file = json.load(file)
		JSON_FILE = file['usage']

'''
Usage Section
'''
def test_copyright():
	regex = re.compile(JSON_FILE['copyright']['regex'], re.M)
	test_list = ["Copyright © Jeremiah Thomas, et al",
				 "\nCopyright © Jeremiah Thomas"
				 "\n\nSome other text",
				 "\nCopyright Jeremiah Thomas, Alexander Jimenez, Eric Bulson"
				 "\n\nSome other text"]
	matches = []
	for test in test_list:
		match = regex.match(test)
		if match is not None:
			matches.append(match.group(1))
	test_answers = ["Jeremiah Thomas, et al", "Jeremiah Thomas", "Jeremiah Thomas, Alexander Jimenez, Eric Bulson"]
	assert matches == test_answers, "USAGE COPYRIGHT - returns wrong string."

def test_license():
	regex = re.compile(JSON_FILE['license']['regex'], re.M)
	test_list = ["Copyright © Jeremiah Thomas, et al"
"\n\nAll rights reserved. All copyright holders retain full copyright individually and may sublicense the work, up to and including a Ø (CC0) declaration."]
	matches = []
	for test in test_list:
		match = regex.match(test)
		if match is not None:
			matches.append(match.group(1))
	test_answers = ["All rights reserved. All copyright holders retain full copyright individually and may sublicense the work, up to and including a Ø (CC0) declaration."]
	assert matches == test_answers, "USAGE LICENSE - returns wrong string."
