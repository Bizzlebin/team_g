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
# Updated 2020-12-06
# 
# +++
# Description
# 
# The main input, parsing, and output script for Readme Parser; requires properly-formatted JSON file (fields.json) to handle a given version of the [NK] Metadata Format.
# 

# 
# +++
# Imports
# 
import os
import sys
import tkinter
from tkinter import filedialog, messagebox
import re
import json
import Queue.linkedqueue as linkedqueue
from datetime import date
# 
# +++
# Assignments
# 
# ===
# Constants
# 
# ---
# Field Names
# 
with open(os.path.join(sys.path[0], 'fields.json'), 'r') as file:
	FIELD_NAMES = json.load(file)	
# 
# +++
# Functions
# 
# ===
# Definitions
# 
# ---
# Input Readme URI
# 
def input_readme_uri(uri: str = None) -> str:
	'''
	Input the location, via Tkinter Open dialog, of the readme to be parsed if it is not already passed (eg, from command line); with basic error handling.

	The dialog will default to "readme.txt" in the last-used [by Tkinter] directory, which may or may not exist. The dialog allows searching for any arbitrary file, including switching from the default .txt to any extension, and should return an OS-independent URI (AKA path).
	'''

	if uri is None:
		root = tkinter.Tk()
		root.withdraw() # Hide/unmake the root window
		uri = filedialog.askopenfilename(title = 'Open Readme', initialfile = 'readme.txt', filetypes = (('Text file', '*.txt'), ('All files', '*.*'))) # Tkinter handles the case where readme.txt doesn't exist with its own built-in warning

	try:
		if uri is not None: # Catch exiting the dialog without selecting a [valid] file
			return uri.replace('/', os.sep) # Tkinter bug: it always returns "*nix"-style paths!; this fixes it
		else:
			raise FileNotFoundError
	except FileNotFoundError:
		input('\n***\n\n**Error**: Readme Parser found no readme file in the current directory! Press Enter to exit...')
		sys.exit() # Automatically creates and handles another exception specifically created for this purpose
# 
# ---
# Create Fields
# 
def create_fields(text, FIELD_NAMES):
	'''
	Create setuptools-compliant fields from the readme using JSON-based regex; handles blank fields but does not tolerate non-compliance.

	All NKMF fields that translate to setuptools fields are captured, with more information in the JSON metadata file. Fields that do not contain data are still sent to the the setup.py file, but as blanks.
	'''

	sections = linkedqueue.LinkedQueue()
	subdivision_names = ['title', 'authorship', 'timestamps', 'usage']
	divisions = re.split(re.compile(FIELD_NAMES['field']['division']['field_regex'], re.M), text)
	subdivisions = re.split(re.compile(FIELD_NAMES['field']['subdivision']['field_regex'], re.M), divisions[0])
	fields = {}

	for (name, subdivision) in zip(subdivision_names, subdivisions):
		sections.add([name, subdivision.strip()])
	for division in divisions:
		if re.search(r'^Description', division.strip()):
			sections.add(['description', division.strip()])

	while not sections.isEmpty():
		section = sections.pop()
		section_name = section[0]
		text = section[1]
		for field in FIELD_NAMES[section_name]:
			if FIELD_NAMES[section_name][field] != 'text/plain' and FIELD_NAMES[section_name][field]['field_regex'] != 'None':
				try:
					match = re.compile(FIELD_NAMES[section_name][field]['field_regex'], re.M).search(text)
					# print(field)
					if match is not None:
						fields[field] = match.group(FIELD_NAMES[section_name][field]['match'])
						# print(match.group(1))
				except (IndexError): # Catch totally blank fields; for filling in later (by function, hand, etc)
					fields[field] = '' # Send blank fields; comment out until """pass""" to send only filled (ie, non-blank) fields
					pass
	return fields
# 
# ---
# Create Strict Snake Case
# 
def create_strict_snake_case(text: str) -> str:
	'''
	Convert an arbitrary string into UEWSG-compliant (and RFC 3986 §2.3-compliant) strict snake case.

	This function takes any string and, using the rules set for for filenames in the UEWSG (and based in turn upon RFC 3986 §2.3, which is nearly a subset of "POSIX-portable" as well, not counting the tilde ("~")), converts it into strict snake case by stripping leading and trailing whitespace, lowercasing all letters, replacing spaces with underscores, and then stripping out any remaining non-compliant characters.
	'''

	NUMBERS = {chr(48 + i) for i in range(10)} # 0–9
	LETTERS = {chr(97 + i) for i in range(26)} # Lowercase only
	OTHERS = {'-', '_', '.', '~'} # Also from RFC 3986 §2.3
	UNRESERVED_CHARACTERS = NUMBERS | LETTERS | OTHERS # From the UEWSG (RFC 3986 §2.3 minus uppercase letters, which aren't part of the UEWSG spec)

	text = text.strip() # Extra whitespace is only permitted in [preformatted] quotes
	text = text.casefold() # Only lowercase letters are permitted in strict snake case
	text = text.replace(' ', '_') # Spaces are replaced with underscores
	for character in text:
		if character not in UNRESERVED_CHARACTERS:
			text = text.replace(character, '') # All non-conforming characters are simply deleted

	return text
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
	uri = input_readme_uri(os.path.join(sys.path[0], 'readme.txt')) # ***Warning***: dummy code!!!
	path = os.path.dirname(uri) # Python leaves all paths OS-specific, so this is required; same as """uri.rsplit(sep = os.sep, maxsplit = 1)[0]""" and a few other methods

	# if os.path.isfile(os.path.join(path, 'setup.py')):
		# try:
			# root = tkinter.Tk()
			# root.withdraw() # Hide/unmake the root window
			# overwrite = messagebox.askokcancel('Warning!', 'A setup.py file already exists in the readme\'s directory; overwrite the current setup.py file?')
			# if overwrite == False:
				# raise UserWarning
		# except UserWarning:
			# input('\n***\n\n**Warning**: Readme Parser is exiting to protect the current setup.py file in the readme\'s directory! Press Enter to exit...')
			# sys.exit()

	try:
		with open(uri, encoding = 'UTF-8') as readme:
			text = readme.read()
	except IOError:
		input('\n***\n\n**Error**: Readme Parser could not open the readme file; please check your file and folder permissions! Press Enter to exit...')
		sys.exit()

	fields = create_fields(text, FIELD_NAMES)
	name = create_strict_snake_case(fields['name']) # Setuptools, PyPI, etc will un-Pythonically not honor underscores—they get replaced with hyphens in *some* places—in the unsemantic mess which is Python packaging and versioning
	name = name.replace('\n', '\n# ')
	for field in fields:
		print(f'**{field}**: {fields[field]}')
	try:
		with open(os.path.join(sys.path[0], 'setup.py'), 'w', encoding = 'UTF-8') as setup:
			setup.write(f'''# Setup | {name}
# 
# For "setuptools" Only
# 
# ***
# 
# By {{author}}
# 
# Generated by Readme Parser
# 
# ***
# 
# Created {date.today().strftime('%Y-%m-%d')}
# 
# +++
# Description
# 
# An auto-generated setup file for {name} by Readme Parser. Remember to fill/add any other fields, as needed. For more information, read the Readme Parser readme and/or in-module documentation.
# 

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
				setup.write(f'\n\t{field} = """{fields[field]}""",')
			setup.write(f'''\n\tlong_description_content_type = """text/plain""",
\tpy_modules = ["""{name}""",],
)''')
		print('\n***\n\nSuccessfully created setup.py!')
		input('\nPress Enter to exit...')
		sys.exit()
	except IOError:
		input('\n***\n\n**Error**: Readme Parser could not create setup.py; please check your file and folder permissions! Press Enter to exit...')
		sys.exit()