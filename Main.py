from tkinter import *
from Helpers.FileHelper import FileHelper
from Models.GasEntry import GasEntry
from Models.Vehicle import Vehicle

file_helper = FileHelper()
file_helper.delete_vehicle(2)
file_helper.delete_gas_entry(2)


window = Tk()


# Code to add widgets will go here...


window.mainloop()
