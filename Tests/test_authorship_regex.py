import json
import re

JSON_FILE = None

def setup_module(module):
	with open('../fields.json', 'r') as file:
		global JSON_FILE
		file = json.load(file)
		JSON_FILE = file['authorship']

'''
Authorship section
'''
def test_author():
	regex = re.compile(JSON_FILE['author']['regex'], re.M)
	test_list = ["By Alexander Jimenez", " By Alex J., et al\n", " By A1@. \n"]
	matches = []
	for test in test_list:
		match = regex.match(test)
		if match is not None:
			matches.append(match.group(1))
	test_answers = ["Alexander Jimenez", "Alex J., et al", "A1@."]
	assert matches == test_answers, "AUTHOR REGEX - returns wrong string."

def test_author_email():
	regex = re.compile(JSON_FILE['author_email']['regex'], re.M)
	test_list = ["By Alexander Jimenez\n\n"
				 "alexanderjimenez@machentertainment.com",
				 " By Alex J., et al\n\n"
				 "alex-j.@us.org",
				 " By A1@. \n\n"
				 "test_@test.tld"]
	matches = []
	for test in test_list:
		match = regex.match(test)
		if match is not None:
			matches.append(match.group(1))
	test_answers = ["alexanderjimenez@machentertainment.com", "alex-j.@us.org", "test_@test.tld"]
	assert matches == test_answers, "AUTHOR EMAIL REGEX - returns wrong string."

