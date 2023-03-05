from tkinter import *
from tkinter import messagebox
from tkinter import ttk


def showInTerminal(*args):
    lbl["text"] = cmbxSelect.get()

root =Tk()

root.geometry(f"{250}x{150}")

cmbx = ttk.Combobox(root)

cmbx["state"] = "readonly"

cmbx.place(x=60, y=50)

cmbxSelect = StringVar()
cmbx['textvariable'] = cmbxSelect
cmbx['values'] = ['Hello', "How are you?", "THIS IS TEXT"]
cmbx.current(0)
cmbx.bind("<<ComboboxSelected>>", showInTerminal)

lbl = Label(root, font="Arial 15")
lbl["text"] = "Здесь выбор"
lbl.place(x=10, y=10)

root.mainloop()