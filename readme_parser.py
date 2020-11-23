# Readme Parser
# 
# https://github.com/Bizzlebin/team_g/blob/master/readme_parser.py
# 
# ***
# 
# By Jeremiah Thomas, et al
# 
# ***
# 
# Created 2020-04-16
# 
# Updated 2020-11-20
# 
# +++
# Description
# 
# The main input, parsing, and output script for Readme Parser; requires properly-formatted JSON file to handle a given version of the [NK] Metadata Format.
# 

# 
# +++
# Imports
# 
from os import sys, path
import re, json
from datetime import date
import Queue.linkedqueue as linkedqueue
import itertools
# 
# +++
# Assignments
# 
with open(path.join(sys.path[0], 'fields.json'), 'r') as file:
    fields_json = json.load(file)
# ===
# Constants
# 
# ---
# Field Names
# 
# FIELD_NAMES = \
#	{
#	'name': (re.compile(fields['name'], re.M), None, ['version', 'url']), # First line is "always" the title (unless escaped), optionally followed by the version and then the container/collection, which in this case will be "assumed" to be a URL; thanks to Nick for help on this: https://stackoverflow.com/questions/61262656/how-can-i-match-work-file-titles-with-optional-elements-using-python-3-regex 
#	'description': (re.compile(fields['description'], re.M), ('Released on', 'http', 'ftp' '***'), []), # Subtitle passed as [short] description; the filters are the beginning of the next [block] fields, preventing an inappropriate match if some fields are left out and these later fields occur earlier than expected
#	'release_date': (re.compile(fields['release_date'], re.M), ('http', 'ftp', '***'), []), # Not currently supported by "setuptools"
#	'download_url': (re.compile(fields['download_url'], re.M), ('***'), []),
#	'license': (re.compile(fields['license'], re.M), None, ['author']), # No need to filter here, given the matching by UEWSG block marker; the author(s) are assumed to be the copyright holders
#	# 'long_description': (re.compile(r'^\+\+\+$.^Description$.^$.(^.+?($.^$.^.+?$)*?$)(?=.^$.^$.^\+\+\+$|.^$.^$.^===$|.^$.^$.^---$|\Z)', re.M | re.S), None, None), # Not sure why this doesn't work; oh well! Using """re.S""" seems to be quite troublesome
#	'license_file': (re.compile(fields['license_file'], re.M), None, []), # Only a chapter marker (or EOF) can follow the license, according to the NKCF, so no more exhaustive checking is needed
#	'long_description': (re.compile(fields['long_description'], re.M), None, []), # "long_description_content_type" is also a valid metadata field that clarifies this one but doesn't seem common; the regex tests for UEWSG block markers to catch the end of this section, if multiple paragraphs are used
#}
FIELD_NAMES = {}

for field_section in fields_json:
	field_regex = fields_json[field_section]["regex"]

	if fields_json[field_section]["filters"]:
		field_filters = fields_json[field_section]["filters"]
	else:
		field_filters = None

	field_subfields = fields_json[field_section]["subfields"]

	FIELD_NAMES[field_section] = (re.compile(field_regex, re.M), field_filters, field_subfields)
# 
# +++
# Functions
# 
# ===
# Definitions
# 
# ---
# Read Readme
# 
def read_readme():
	filenames = ('readme', 'README') # Necessary for case-sensitive file systems; weird caps are just SOL
	extensions = ('.txt', '') # Accept non-UEWSG-recommended lack of file extension

	try:
		for name in filenames:
			for ext in extensions:
				if path.exists(f'{name}{ext}'):
					return path.join(sys.path[0], f'{name}{ext}') # """path.join()""" handles MS-DOS-style vs POSIX-compliant paths while """sys.path[0]""" gets the correct CWD if running the script via another program (eg, as a "Run" command/shortcut in Notepad++)
		else:
			raise OSError
	except OSError:
		input('**Error**: Readme Parser found no readme file in the current directory! Press Enter to exit...')
		sys.exit() # Automatically creates and handles another exception specifically created for this purpose
# 
# ---
# Read Fields
# 
def read_fields(text, FIELD_NAMES):
	fields = linkedqueue.LinkedQueue()
	start = 0

	section_names = ['Title', 'Authorship', 'Timestamps', 'Usage', 'Description']
	sections = re.split(r'[*+=]{3}', text)
	for (name, section) in zip(section_names, sections):
		fields.add([name, section.strip()])
	
	for field in FIELD_NAMES:
		subfields = FIELD_NAMES[field][2]
		try:
			match = FIELD_NAMES[field][0].search(text, start)
			if FIELD_NAMES[field][1]:
				filters = FIELD_NAMES[field][1]
			else:
				filters = '' # This not only gets rid of a """TypeError""" iterating on """None""" but doesn't have a negative effect when trying to filter—perhaps zero-length strings don't compare?
			for filter in filters:
				if filter in match.group(1)[:len(filter)]:
					fields.add([field, '']) # Send blank fields; comment out to send only filled
					break
			else:
				start = match.end()
				if match.group(1) is None:
					fields.add([field, '']) # Prevent """None""" from being sent
				else:
					fields.add([field, match.group(1)])
				if subfields:
					for i in range(len(subfields)):
						if match.group(i + 2) is None:
							fields.add([subfields[i], '']) # Prevent """None""" from being sent
						else:
							fields.add([subfields[i], match.group(i + 2)]) # The first group is already the main field so start at group 2
		except AttributeError: # Catch totally blank fields that can't be regexed; for filling in later (by function, hand, etc)
			fields.add([field, '']) # Comment out until """pass""" to send only filled (ie, non-blank) fields
			if subfields:
				for i in range(len(subfields)):
					fields.add([subfields[i], ''])
			pass
	return fields
# 
# +++
# Output
# 
if __name__ == '__main__':
	print('''Readme Parser

Make "setup.py" Easy!

+++
Output
''')
	try:
		with open(read_readme(), encoding = 'UTF-8') as readme:
			text = readme.read()
	except IOError:
		input('\n***\n\n**Error**: Readme Parser could not open the readme file; please check your file and folder permissions! Press Enter to exit...')
		sys.exit()
	fields = read_fields(text, FIELD_NAMES)
	name = fields.peek()[1] # Since name is used several times I decided to create a variable for it to accomadate the queue structure more easily. 2020-11-18 Eric Bulson
	name = name.casefold().replace(' ', '_') # Setuptools, PyPI, etc will un-Pythonically not honor underscores—they get replaced with hyphens in *some* places—but this is a best-effort solution to deal with the unsemantic mess which is Python packaging and versioning; case is otherwise normalized, as per the UEWSG
	for field in range(0, (fields.__len__()-1)):
		field = fields.pop()
		print(f'**{field[0]}**: {field[1]}')
		fields.add(field)
	try:
		with open(path.join(sys.path[0], 'setup.py'), 'w', encoding = 'UTF-8') as setup:
			setup.write(f'''# Setup | {name}
# 
# For "setuptools" only
# 
# {date.today().strftime('%Y-%m-%d')}
# 
# ***
# 
# Generated by Readme Parser
# 
# +++
# Description
# 
# An auto-generated setup file for {name} by Readme Parser. Remember to fill/add any other fields, as needed. For more information, read the Readme Parser readme and/or in-module documentation.
# 
# +++
# Imports
# 
from setuptools import setup
# 
# +++
# Output
# 
setup(''')
			for field in fields:
				field = fields.pop()
				setup.write(f'\n\t{field[0]} = """{field[1]}""",')
			setup.write(f'''\n\tlong_description_content_type = """text/plain""",
\tpy_modules = ["""{name}""",],
)''')
		print('\n***\n\nSuccessfully created setup.py!')
		input('\nPress Enter to exit...')
		sys.exit()
	except IOError:
		input('\n***\n\n**Error**: Readme Parser could not create setup.py; please check your file and folder permissions! Press Enter to exit...')
		sys.exit()
# 
# +++
# Old NKMF
# 
# A brief overview of the header of an *old* NKMF-compliant document, for testing the JSON on an old-style readme early on in the project:
# 
# """
# [Title[ *semantic* version][ | Container/Collection (after *literal* vertical bar/pipe)]]
# 
# [Subtitle]
# 
# [[Released on ]YYYY[-MM[-DD]]]
# 
# [(Download) URL]
# 
# ***
# 
# [[Ø|[Copyright ]© ][YYYY ]Author(s)]
# 
# [Full license]
# 
# +++
# Description
# 
# [What, briefly how, and rarely why]
# 
# ===
# Changelog
# 
# [Brief version history and highlights by number—exhaustive diffs are for Git! Use numbered or description lists, eg "**Version 0.1.0**:[ (YYYY[-MM[-DD]])] First release. Started adding..."]
# """