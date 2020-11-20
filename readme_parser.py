# Readme Parser 0.3.0
# 
# Make "setup.py" Easy!
# 
# https://github.com/Bizzlebin/team_g
# 
# ***
# 
# By JBT, et al
# 
# ***
# 
# Created 2020-11-17
# 
# +++
# Description
# 
# A basic parser to extract setup.py metadata fields from a NKMF-compliant (and UEWSG-compliant!) UTF-8 readme file. Fields must not be [preformatted] blockquotes—they are difficult to parse (at present). Assumes 1 script with same snake-case name as """name""". If using the legacy distutils.core, fields must be "short strings", under 200 characters, to be compatible with the (setuptools does not appear to have this restriction). The """name""", """version""", and """url""" fields are required for distutils.
#
# Some fields will need to be manually added. There is no consistent way to add an e-mail address since it is not part of the NKMF at present. Similarly, other fields are not part of the NKMF and/or are just not very useful for the majority of projects; make sure to check project requirements. Finally, note the below fields, which can be generated programmatically (eg, using the vermin library) but are outside the scope of this parser:
# 
# • """install_requires = ['my_package >=8.34']"""
# • """python_requires = '>=3.9'"""
# 

# 
# +++
# Imports
# 
from os import sys, path
import re, json
from datetime import date
import Queue.linkedqueue as linkedqueue
# 
# +++
# Assignments
# 
with open(path.join(sys.path[0], 'fields.json'), 'r') as file:
    fields = json.load(file)
# ===
# Constants
# 
# ---
# Field Names
# 
# Syntax: 'name': {regex_for_field, (filters)|None, [subfields_in_regex_groups]}
# 
# The number of capturing groups, if greater than 1, *must* match the number of subfields; subfields *must* be lists, not tuples, or single-value contents will be indexed as a plain string! Fields names are roughly adjusted to match the "setuptools" (successor to "distutils") metadata fields, found at https://setuptools.readthedocs.io/en/latest/setuptools.html# metadata .
# 
FIELD_NAMES = \
	{
	'name': (re.compile(fields['name'], re.M), None, ['version', 'url']), # First line is "always" the title (unless escaped), optionally followed by the version and then the container/collection, which in this case will be "assumed" to be a URL; thanks to Nick for help on this: https://stackoverflow.com/questions/61262656/how-can-i-match-work-file-titles-with-optional-elements-using-python-3-regex 
	'description': (re.compile(fields['description'], re.M), ('Released on', 'http', 'ftp' '***'), []), # Subtitle passed as [short] description; the filters are the beginning of the next [block] fields, preventing an inappropriate match if some fields are left out and these later fields occur earlier than expected
	'release_date': (re.compile(fields['release_date'], re.M), ('http', 'ftp', '***'), []), # Not currently supported by "setuptools"
	'download_url': (re.compile(fields['download_url'], re.M), ('***'), []),
	'license': (re.compile(fields['license'], re.M), None, ['author']), # No need to filter here, given the matching by UEWSG block marker; the author(s) are assumed to be the copyright holders
	# 'long_description': (re.compile(r'^\+\+\+$.^Description$.^$.(^.+?($.^$.^.+?$)*?$)(?=.^$.^$.^\+\+\+$|.^$.^$.^===$|.^$.^$.^---$|\Z)', re.M | re.S), None, None), # Not sure why this doesn't work; oh well! Using """re.S""" seems to be quite troublesome
	'license_file': (re.compile(fields['license_file'], re.M), None, []), # Only a chapter marker (or EOF) can follow the license, according to the NKCF, so no more exhaustive checking is needed
	'long_description': (re.compile(fields['long_description'], re.M), None, []), # "long_description_content_type" is also a valid metadata field that clarifies this one but doesn't seem common; the regex tests for UEWSG block markers to catch the end of this section, if multiple paragraphs are used
}
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
# 
# +++
# Changelog
# 
# **0.3.0**: (2020-11-17) Converted to a group project (WTCC CSC 130-001), ...
# **0.2.5**: (2020-04-27) Finished lots of iterations trying to figure out eggs, PIP, and grammar issues (eg, capitalization and underscores vs hyphens)—an alternative to PIP may be necessary
# **0.2.4**: (2020-04-25) More testing/fiddling
# **0.2.3**: (2020-04-25) More testing/fiddling
# **0.2.2**: (2020-04-25) More testing/fiddling
# **0.2.1**: (2020-04-25) Started testing for distutils, playing with setup.cfg, etc
# **0.1.1**: (2020-04-25) No change (started experiments with PIP, etc)
# **0.1.0**: (2020-04-16) Initial version
# 
# +++
# Todo
# 
# • Update to latest version of NKMF
# • Add in "dummy" regexes to capture dinkuses solely for the purpose of moving up start position?
# • Fix "Description" becoming license text if license text is missing
# • Add flags for running in interactive mode, test mode (ie, show only parse without making setup.py)—default should be to run silently
# • Parse filters with regex, allowing for more dynamic filtering
# • Escaped title (as per UEWSG) compatibility?
# • Would the field names be better as JSON?
