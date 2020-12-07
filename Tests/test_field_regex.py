import json
import re

JSON_FILE = None

def setup_module(module):
	with open('../fields.json', 'r') as file:
		global JSON_FILE
		file = json.load(file)
		JSON_FILE = file['field']

def test_field_section():
	# Import JSON
	test_text = "SECTION 1\n" \
				"+++\n" \
				"\n" \
				"\n" \
				"NEW SECTION WITH EXTRA PADDING.\n" \
				"\n" \
				"\n" \
				"+++\n" \
				"LAST SECTION WITH LACK OF PADDING"
	test_answer = ["SECTION 1\n",
				   "\n\n\nNEW SECTION WITH EXTRA PADDING.\n\n\n",
				   "\nLAST SECTION WITH LACK OF PADDING"]

	sections = re.split(JSON_FILE['division']['regex'], test_text)
	assert sections == test_answer, "FIELD REGEX - returns wrong string."
