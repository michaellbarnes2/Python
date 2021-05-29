from pathlib import Path
from Tkinter import *
master = Tk()

def var_states():
   print("Dev: %d,\nProd: %d" % (var1.get(), var2.get()))
   myfile = open("myfile5b.txt", "w+")
   myfile.write("dev deployment")
   myfile.write("prod deployment")
   myfile.write("Dev: %d,\nProd: %d" % (var1.get(), var2.get()))
   myfile.close()



Label(master, text="Environment:").grid(row=0, sticky=W)
var1 = IntVar()
Checkbutton(master, text="Dev", variable=var1).grid(row=1, sticky=W)
var2 = IntVar()
Checkbutton(master, text="Prod", variable=var2).grid(row=2, sticky=W)
Button(master, text='Quit', command=master.quit).grid(row=3, sticky=W, pady=4)
Button(master, text='Show', command=var_states).grid(row=4, sticky=W, pady=4)

mainloop()