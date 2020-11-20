Readme Parser 0.3.0

Make "setup.py" Easy!

https://github.com/bizzlebin/team_g/

***

By Jeremiah Thomas, et al

***

Created 2020-04-16

Updated 2020-11-20

***

Copyright © Jeremiah Thomas, et al

All rights reserved. All copyright holders retain full copyright individually and may sublicense the work, up to and including a Ø (CC0) declaration.

"""THE WORK IS PROVIDED "AS IS" AND THE AUTHORS AND OWNERS DISCLAIM ALL WARRANTIES WITH REGARD TO THIS WORK INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHORS OR OWNERS BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS WORK."""

+++
Description

A basic parser to extract setup.py metadata fields from a NKMF-compliant (and UEWSG-compliant!) UTF-8 readme file.

===
Constraints

Fields must not be [preformatted] blockquotes—they are difficult to parse (at present). Assumes 1 script with same snake-case name as """name""". If using the legacy distutils.core, fields must be "short strings", under 200 characters, to be compatible with the (setuptools does not appear to have this restriction). The """name""", """version""", and """url""" fields are required for distutils.

Some fields will need to be manually added. There is no consistent way to add an e-mail address since it is not part of the NKMF at present. Similarly, other fields are not part of the NKMF and/or are just not very useful for the majority of projects; make sure to check project requirements. Finally, note the below fields, which can be generated programmatically (eg, using the vermin library) but are outside the scope of this parser:

• """install_requires = ['my_package >=8.34']"""
• """python_requires = '>=3.9'"""

===
JSON Fields Format

The JSON file must contain all applicable fields in a dict with their setuptools name as the key; setuptools is the successor to distutils, found at https://setuptools.readthedocs.io/en/latest/setuptools.html#metadata . """filters""" are lists of strings or null and """subfields""" are lists of 0 or more strings (they *must* match the capturing groups of the regex).

"""
{
	"": {
		"regex": "",
		"filters": "",
		"subfields": ""
	}
}
"""

+++
Changelog

**0.3.0**: (2020-11-17) Converted to a group project (WTCC CSC 130-001), ...
**0.2.5**: (2020-04-27) Finished lots of iterations trying to figure out eggs, PIP, and grammar issues (eg, capitalization and underscores vs hyphens)—an alternative to PIP may be necessary
**0.2.4**: (2020-04-25) More testing/fiddling
**0.2.3**: (2020-04-25) More testing/fiddling
**0.2.2**: (2020-04-25) More testing/fiddling
**0.2.1**: (2020-04-25) Started testing for distutils, playing with setup.cfg, etc
**0.1.1**: (2020-04-25) No change (started experiments with PIP, etc)
**0.1.0**: (2020-04-16) Initial version

+++
Todo

• Update to latest version of NKMF
• Fix "Description" becoming license text if license text is missing
• Add flags for running in interactive mode, test mode (ie, show only parse without making setup.py)—default should be to run silently

+++
Metametadata

**meta_title**: Readme
**meta_uri**: https://github.com/bizzlebin/team_g/blob/master/readme.txt
**meta_author**: Jeremiah Thomas
**meta_created**: 2020-11-16
**meta_updated**: 2020-11-20