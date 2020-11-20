import tkinter
from tkinter import filedialog, messagebox

root = tkinter.Tk()
root.withdraw() # Hide/unmake the root window
uri = tkinter.filedialog.askopenfilename(title = 'Open Readme', initialfile = 'readme.txt', filetypes = (('Text file', '*.txt'), ('All files', '*.*'))) # Tkinter handles the case where readme.txt doesn't exist with its own built-in warning

path = uri.rsplit(sep = '/', maxsplit = 1)[0] # Handles only Windows paths; please fix this
override = tkinter.messagebox.showerror('Warning!', 'A setup.py file already exists in the readme\'s directory; overwrite the current setup.py file?')

print(uri)
print(path)
print(override)