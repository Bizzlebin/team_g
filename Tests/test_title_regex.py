import json
import re

JSON_FILE = None

def setup_module(module):
	with open('../fields.json', 'r') as file:
		global JSON_FILE
		file = json.load(file)
		JSON_FILE = file['title']

'''
Title Section
'''
def test_name():
	regex = re.compile(JSON_FILE['name']['regex'], re.M)
	test_list = ["Test Name 0.0.1", " Ubuntu: Disco Dingo! 19.04\nDisco dog", " Title w/ no version... \n"]
	matches = []
	for test in test_list:
		match = regex.match(test)
		if match is not None:
			matches.append(match.group(1))
	test_answers = ["Test Name", "Ubuntu: Disco Dingo!", "Title w/ no version..."]
	assert matches == test_answers, "NAME REGEX - returns wrong string."

def test_version():
	regex = re.compile(JSON_FILE['version']['regex'], re.M)
	test_list = ["Test Name 0.0.1", " Ubuntu: Disco Dingo! 19.04\nDisco Time", " Title w/ no version... \n"]
	matches = []
	for test in test_list:
		match = regex.match(test)
		if match is not None:
			matches.append(match.group(1))
	test_answers = ["0.0.1", "19.04", ""]
	assert matches == test_answers, "VERSION REGEX - returns wrong string."

def test_url():
	regex = re.compile(JSON_FILE['url']['regex'], re.M)
	test_list = ["\nReadme Parser 0.3.0 | http://example.com\nDO NOT PARSE ME", " Ubuntu Disco Dingo! 19.04 | https://ubuntu.com/", "NK Metadata Format |  uri://nkmf.org", "Query Site | https://www.google.com/search?hl=en&authuser=0"]
	matches = []
	for test in test_list:
		match = regex.match(test)
		if match is not None:
			matches.append(match.group(1))
	test_answers = ["http://example.com", "https://ubuntu.com/", "uri://nkmf.org", "https://www.google.com/search?hl=en&authuser=0"]
	assert matches == test_answers, "URL REGEX - returns wrong string."

def test_description():
	regex = re.compile(JSON_FILE['description']['regex'], re.M)
	test_list = ["\nThis is a test description",
				 "\n Errant whitespace checks in.\n"
				 "Don't parse me though.",
				 "\nTraditional example.\nhttp://example.com/"]
	matches = []
	for test in test_list:
		match = regex.match(test)
		if match is not None:
			matches.append(match.group(1))
	test_answers = ["This is a test description",
				 "Errant whitespace checks in.",
				 "Traditional example."]
	assert matches == test_answers, "DESCRIPTION REGEX - returns wrong string."

def test_download_url():
	regex = re.compile(JSON_FILE['download_url']['regex'], re.M)
	test_list = ["\nThis is a test description"
				 "\n\nftp://filezilla.net/",
				 "\r Errant whitespace checks in."
				 "\n\n ukmf://nontraditional-uri.tld\ "
				 "\n\nDon't parse me though.",
				 "\nTraditional example."
				 "\n\nhttp://example.com/"]
	matches = []
	for test in test_list:
		match = regex.match(test)
		if match is not None:
			matches.append(match.group(1))
	test_answers = ["ftp://filezilla.net/",
				 "ukmf://nontraditional-uri.tld",
				 "http://example.com/"]
	assert matches == test_answers, "DOWNLOAD URL - Regex returns wrong string."

