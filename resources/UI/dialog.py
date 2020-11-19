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
import os

#
# +++
# Functions
#
# ===
# Definitions
#
# ---
# Interface
#
class Interface(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.file_path = tk.StringVar()
        self.file_path.set((os.getcwd() + "\\readme.txt"))
        self.master = master
        self.pack()
        self.file_frame()
#
# ---
# file dialog
#
    def file_dialog(self):
        file_window = fd.askopenfilename(initialdir=".", filetypes=(("Text Files", ".txt"), ("All Files", "*.*")))
        if file_window != "":
            self.file_path.set(file_window)
#
# ---
# reset file selection
#
    def reset_file_selection(self):
        self.file_path.set((os.getcwd() + "\\readme.txt"))
#
# ---
# submit file
#
    def submit_file(self):
        pass
#
# ---
# file frame
#
    def file_frame(self):
        frame = tk.Frame()
        frame.pack()
        file_path_field = tk.Entry(frame, width=40, textvariable=self.file_path)
        open_file_button = tk.Button(frame, text="Browse", command=self.file_dialog)
        reset_button = tk.Button(frame, text="Reset", command=self.reset_file_selection)
        okay_button = tk.Button(frame, text="Okay", command=self.submit_file)
        file_path_field.pack(side="left")
        open_file_button.pack(side="left")
        reset_button.pack(side="left")
        okay_button.pack(side="left")


root = tk.Tk()
app = Interface(master=root)
app.master.title("Prototype Interface")
app.master.minsize(400, 400)
app.master.maxsize(400, 400)
app.mainloop()

#
# +++
# Todo
#
# • Find out how to change os.getcwd from "\" to "/" on Windows systems.
# • Rename "Okay" button to something a little more appropriate.
