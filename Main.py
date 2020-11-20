from tkinter import *
from Helpers.FileHelper import FileHelper
from Models.GasEntry import GasEntry
from Models.Vehicle import Vehicle

file_helper = FileHelper()
# vehicle = Vehicle('test', 2000, 'test', 'test', 'test')
# gas_entry = GasEntry(1, '11/12/2020', 123456, 1.25, 2.09)
# file_helper.save_vehicle(vehicle)
# file_helper.save_gas_entry(gas_entry)
file_helper.delete_vehicle(2)
file_helper.delete_gas_entry(2)


window = Tk()


# Code to add widgets will go here...


window.mainloop()
