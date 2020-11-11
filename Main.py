import tkinter
from Helpers.FileHelper import FileHelper
from Models.GasEntry import GasEntry
from Models.Vehicle import Vehicle

file_helper = FileHelper()
entry = GasEntry(1, '11/10/2020', 166768, 9.863, 2.099)
vehicle = Vehicle('Dodge Dakota', 2001, 'Dodge', 'Dakota', 'black')
file_helper.save_gas_entry(entry)
file_helper.save_vehicle(vehicle)


window = tkinter.Tk()


# Code to add widgets will go here...


window.mainloop()
