# Interface
#
# dialog.py
#
# ***
#
# By Alexander Jimenez
#
# ***
#
# Created 11/17/2020
#
# Updated 11/18/2020
#
# +++
# Description
#
# Create an interface for users to point the program to their readme file. Uses tkinter.
#

#
# +++
# Imports
#
import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox as md
import os

#
# +++
# Functions
#
# ===
# Definitions
#
# ---
# File Dialog
#
def file_dialog():
    '''
    Prompt the user for a file.
    Return text: str file path to selected file.
    '''
    root = tk.Tk()
    root.withdraw()
    file = fd.askopenfilename(title = 'Open Readme', initialfile = 'readme.txt', filetypes = (('Text file', '*.txt'), ('All files', '*.*')))
    return file
#
# ---
# alert
#
def alert_dialog():
    '''
    Prompt the user that setup.py was already found. Has no file logic, only prompts.
    Return text: bool True to if okay to overwrite, False is user canceled.
    '''
    root = tk.Tk()
    root.withdraw()
    override = md.askokcancel("Setup.py Already Found!", "Setup.py already found! Did you want to overwrite the file?")
    return override
#
# +++
# Todo
#
# Changelog
#
# **0.2.0**: (2020-11-19) Refactor for simplicity
# **0.1.0**: (2020-11-18) Initial prototype