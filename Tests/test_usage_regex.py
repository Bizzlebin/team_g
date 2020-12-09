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

def test_license():
	regex = re.compile(JSON_FILE['license']['regex'], re.M)
	test_list = ['Copyright © Jeremiah Thomas, et al'
				 '\n\nAll rights reserved. All copyright holders retain full copyright individually and may sublicense the work, up to and including a Ø (CC0) declaration.'
				 '\n\n"""THE WORK IS PROVIDED "AS IS" AND THE AUTHORS AND OWNERS DISCLAIM ALL WARRANTIES WITH REGARD TO THIS WORK INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHORS OR OWNERS BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS WORK."""']
	matches = []
	for test in test_list:
		match = regex.match(test)
		if match is not None:
			matches.append(match.group(1))
	test_answers = ['Copyright © Jeremiah Thomas, et al'
				 '\n\nAll rights reserved. All copyright holders retain full copyright individually and may sublicense the work, up to and including a Ø (CC0) declaration.'
				 '\n\n"""THE WORK IS PROVIDED "AS IS" AND THE AUTHORS AND OWNERS DISCLAIM ALL WARRANTIES WITH REGARD TO THIS WORK INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHORS OR OWNERS BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS WORK."""']
	assert matches == test_answers, "USAGE LICENSE - returns wrong string."
