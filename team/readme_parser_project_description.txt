Readme Parser: Project Description

https://github.com/bizzlebin/team_g/blob/master/team/readme_parser_project_description.txt

***

By Jeremiah Thomas, Eric Bulson, Alexander Jimenez

***

Created 2020-11-30

Updated 2020-12-01

+++

Readme Parser, subtitled with the tagline "Make 'setup.py' Easy!", is a basic parser designed to extract setup.py metadata fields from NK-Metadata-Format-compliant (and UEWSG-compliant!) UTF-8 readme files. With a minimal, user-friendly UI and comprehensive error handling, the program can output a valid setup.py file with as little as one click. No special user knowledge is required: the parser instantly handles all the intricacies of the setup.py file and the setuptools package format. Though parts of this project were prototyped earlier in the school year, it was overhauled to use Tkinter dialogs, the most recent version of the NKMF, and an external JSON file. For its fundamental data type, the parser now uses a queue.

Before (readme.txt) | After (setup.py)

The immediate goal of Readme Parser is to create setup.py files with as little work and extra overhead as possible: by automating the process, software developers can more quickly package and release their code for others to use either locally, with PIP, or on another Python-compatible package manager. By eliminating one of the more error-prone frustrating parts of Python development, the world of coding is therefore opened up to more people than ever and becomes more accessible—and more accessible even for veteran developers.

The larger goal of the program is to promote sustainable documentation practices more generally, including the New Kidron Metadata Format and Uniform English Writing Style Guide. With programmers under assault by more and more superfluous frameworks and markup regimes (eg, Markdown), Readme Parser is designed to help restore one of the original promises of digital documentation: single source of truth. With the parser and the associated standards, it is no longer necessary to duplicate information in either content or format: one single text file in plain language is enough to programmatically produce everything from setup files (Readme Parser) to fully-compliant HTML5 webpages (UEWSG Parser, a sister project) without any user intervention. In a way, the parser brings automation to language itself.

To reach that goal, the program uses a queue: of all the data types available, a queue is the best fit for the algorithm. In order to parse a readme, Readme Parser first needs to extract the different NKMF divisions: the title information, the authorship data, and so on. This extraction is done serially, just as a person might read the document. Later, the divisions need to be parsed again, serially, to extract the setup.py fields as specified in the setuptools documentation; this also occurs in a first-in, first-out scheme, based on the order given in the NKMF but translated into the form usable by setuptools. Nearly every step of the program is linear, from input to output. With such clear requirements, a queue is the logical choice. The overhead of a heavy, class-based queue may outweigh the benefits for a project as small as this, but the utility of the queue, from a computer science point of view, is clear in this application.

+++
Metadata

===
Description

The group paper for the project. The requirements are "Submit a one to two page description of your project, including what your program is designed to do and what data structures you use."; no format was specified, meaning we'll likely submit this paper converted into a universal, open document format like ODT and use the NKMF with UEWSG for the semantics and styling.