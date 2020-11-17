# Input Int 2.2.0
# 
# input_int.py
# 
# ***
# 
# By Jeremiah Thomas
# 
# ***
# 
# Created 2020-08-19
# 
# Updated 2020-11-12
# 
# +++
# Description
# 
# A small module to simplify the process of obtaining a valid integer from the user; with basic error checking/handling.
# 
# Verifying user input is incredibly common in programs, so this is a function I have used, in one form or another, since CSC 121 in 2H 2019; this particular, streamlined implementation—with parameters to make it more customizable—traces back to CSC 256 .
# 

# 
# +++
# Imports
# 
from typing import Optional
# 
# +++
# Functions
# 
# ===
# Definitions
# 
# ---
# Input Int
# 
def input_int \
	(
	prompt: str,
	min: float = float('-inf'),
	max: float = float('inf'),
	error: str = 'That is not a valid number!',
	escape: str = None
	) -> Optional[int]:
	'''
	Get a valid integer from the user.

	This function repeatedly asks the user for an integer using an arbitrary prompt, passed as an argument, until the input is valid or matches the escape string. The minimum and maximum valid numbers, inclusive, are fully tunable. All non-integers raise exceptions, as do invalid numbers; the function and error-handling are completely self-contained and the error message can be customized.
	'''

	while True:
		string: str = input(prompt)
		if string == escape:
			return None
		try:
			number: int = int(string)
			if number < min:
				raise ValueError
			if number > max:
				raise ValueError
			return number
		except ValueError:
			print(error)
# 
# +++
# Output
# 
if __name__ == '__main__':
	while True:
		print(input_int('"""input_int()""" driver: '))
# 
# +++
# Changelog
# 
# **2.2.0**: (2020-11-12) Added driver for quick testing.
# **2.1.0**: (2020-11-11) Added type annotations so the docstring follows the new format: no more redundant parameter and return documentation! Further, the parameters now follow the Whitesmiths style, as per the [NK]CF (version 2020-10-17), for easier readability.
# **2.0.0**: (2020-09-16) Renamed to input_int.py (as per [NK] Code Format CURD-based naming conventions), changed return to """None""" on escape for more consistent return handling.
# **1.0.0**: (2020-08-19) Derived from get_float.py, which was originally created for CSC 256 earlier the same day.