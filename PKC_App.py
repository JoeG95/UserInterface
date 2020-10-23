from tkinter import *
from tkinter import messagebox as MessageBox

app = Tk()
app.minsize(1880,1010)
app.resizable(0,0)
app.title('Pick to Light System')
app.config(bg = 'light blue', bd = 15, relief = 'groove')
app.iconbitmap('HARNESS ENGINE.ico')

#------------------------------------------------------Functions--------------------------------------------------------

def operationA():
    MessageBox.showinfo('Connector A', 'Starting sequence')
    print('Starting')

def operationB():
    MessageBox.showinfo('Connector B', 'Starting sequence')
    print('Starting')

def close():
    result = MessageBox.askquestion('Exit', 'Do you want to leave?')
    if result == 'yes':
        MessageBox.showinfo('Good bye', 'Finishing test')
        app.destroy()
    else:
        MessageBox.showinfo('Stay', 'Process will conitnue')

#------------------------------------------------------Pictures---------------------------------------------------------

picA = PhotoImage(file = "Connector1.png")
picB = PhotoImage(file = "Connector2.png")

#--------------------------------------------------------Labels---------------------------------------------------------

title = Label(app, text = "Please Select a Connector Part Number: ")
title.config(
    bg = "light blue",
    fg = "black",
    font = ("Arial Black", 20)
)
title.grid(row = 0, column = 0, columnspan = 12, padx = 0, pady = 0)

ConA = Label(app, image = picA)
ConA.grid(
    row = 1,
    column = 0,
    padx = 0,
    pady = 0
)

ConB= Label(app, image = picB)
ConB.grid(
    row = 1,
    column = 1,
    padx = 0,
    pady = 0
)

infoA= Label(app, text = "Oracle Number: 199022")
infoA.config(
    bg = "light blue",
    fg = "black", font = ("Arial Black", 12)
)
infoA.grid(row = 2, column = 0, padx = 0, pady = 0)

infoB= Label(app, text = "Oracle Number: 970381")
infoB.config(
    bg = "light blue",
    fg = "black",
    font = ("Arial Black", 12)
)
infoB.grid(row = 2, column = 1, padx = 0, pady = 0)

#--------------------------------------------------------Buttons--------------------------------------------------------

optA = Button(app, text = "First Connector", width = 30, height = 5, command = operationA)
optA.config(
    bg = "light yellow",
    fg = "black",
    font = ("Arial Black", 14)
)
optA.grid(row = 3, column = 0, padx = 0, pady = 0, ipadx = 0, ipady = 0)

optB = Button(app, text = "Second Connector", width = 30, height = 5, command = operationB)
optB.config(
    bg = "light yellow",
    fg = "black",
    font = ("Arial Black", 14)
)
optB.grid(row = 3, column = 1, padx = 0, pady = 0, ipadx = 0, ipady = 0)

optC = Button(app, text = "Close App", width = 30, height = 5, command = close)
optC.config(
    bg = "light yellow",
    fg = "black",
    font = ("Arial Black", 14)
)
optC.grid(row = 4, column = 0, padx = 0, pady = 0, ipadx = 0, ipady = 0)

app.mainloop()