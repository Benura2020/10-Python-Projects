"""
Modules - tkinter, tkcalendar

"""

from tkinter import *
from tkcalendar import *

#creating the window application

root = Tk()

#Set a title to application

root.title("CALENDAR")

#set dimensions

root.geometry("500x300")

cal = Calendar(root, year=2023, month=8, day=10)
#paddings
cal.pack(padx=5,pady=5)

root.mainloop()