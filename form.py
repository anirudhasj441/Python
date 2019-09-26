from tkinter import *

root = Tk()
Label(root,text = '').grid(row=0,column = 0)
Label(root,text = 'Name:').grid(row=1,column = 0)
name = Entry(root).grid(row=1,column=1)
Label(root,text = 'Roll No:').grid(row=2,column = 0)
roll_no = Entry(root).grid(row=2,column=1)
cl = Listbox(root).grid(row=3,column=1)

root.mainloop()