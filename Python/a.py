#!/usr/bin/env python3.7

import os
from tkinter import *
from Append import *
from tkinter import ttk

def converter():
    os.system('/home/chiren/Downloads/Python/converter.sh')

os.system('rm /home/chiren/Downloads/Python/Diet.txt')
root = Tk()

# This will set the geometry to 200x100
root.geometry('250x130')

text1 = StringVar()
text2 = StringVar()

# These text are used to set initial
# values of Checkbutton to off
text1.set('Mango-Chutney')
text2.set('Brown biryani Rice')

chkbtn1 = ttk.Checkbutton(root, textvariable = text1, variable = text1,
                          offvalue = 'Mango-Chutney',
                          onvalue = 'Done',command = test)

chkbtn1.pack(side = TOP, pady = 10)
chkbtn2 = ttk.Checkbutton(root, textvariable = text2, variable = text2,
                          offvalue = 'GFG Average',
                          onvalue = 'Done',command=test2)
chkbtn2.pack(side = TOP, pady = 10)
B=Button(root,text="Convert",command=converter)
B.pack()
root.mainloop()

