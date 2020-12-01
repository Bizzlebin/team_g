Readme Parser: Project Description

https://github.com/bizzlebin/team_g/blob/master/team/readme_parser_project_description.txt

***

By Jeremiah Thomas, Eric Bulson, Alexander Jimenez

***

Created 2020-11-30

+++

Readme Parser, subtitled with the tagline "Make 'setup.py' Easy!", is a basic parser designed to extract setup.py metadata fields from NK-Metadata-Format-compliant (and UEWSG-compliant!) UTF-8 readme files. With a minimal, user-friendly UI and comprehensive error handling, the program can output a valid setup.py file with as little as one click. No special user knowledge is required: the parser instantly handles all the intricacies of the setup.py file and the setuptools package format. Though this project was prototyped earlier in the year, it was overhauled to use Tkinter dialogs, the most recent version of the NKMF, and an external JSON file. For its fundamental data type, the parser uses a queue.

Of all the data types available, the queue makes the most sense for the program. In order to parse a readme, Readme Parser first needs to extract the different NKMF divisions: the title information, the authorship data, and so on. This extraction is done serially, just as a person might read the document. Later, the divisions need to be parsed again, serially, to extract the setup.py fields as specified in the setuptools documentation; this also occurs in a first-in, first-out scheme, based on the order given in the NKMF but translated into the form usable by setuptools. Nearly every step of the program is linear, from input to output. With such clear requirements, a queue was the logical choice. The overhead of a heavy, class-based queue may outweigh the benefits for a project as small as this, but the utility of the queue, from a computer science point of view, is clear in this application.

+++
Metadata

===
Description

The group paper for the project. The requirements are "Submit a one to two page description of your project, including what your program is designed to do and what data structures you use."; no format was specified, meaning we'll likely submit this paper converted into a universal, open document format like ODT and use the NKMF with UEWSG for the semantics and styling.