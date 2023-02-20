from tkinter import *
from tkinter import ttk

DistanceFile = open('numsDistance','r')
WeightFile = open('numsWeight','r')

Conversions = ['Distance','Distance','Weight','Volume']
DistanceUnits = {'':0,'Inches':1,'Feet':2,'Yards':3,'Miles':4,'Centimeters':5,'Meters':6,'Kilometers':7}
WeightUnits = {'':0,'Ounces':1,'Pounds':2,'Tons':3,'Milligrams':4,'Grams':5,'Kilograms':6,'Metric Tons':7}

tk = Tk()
tk.title("Conversion")
tk.geometry('250x120')
unit1 = StringVar(tk)
unit2 = StringVar(tk)
oper = StringVar(tk)

def setunits(*args):
    unit1.set('')
    unit2.set('')
    for i in range(0,len(Conversions)):
        if(oper.get()=='Distance'):
            option1 = ttk.OptionMenu(mainframe, unit1, *DistanceUnits.keys(), command = calculate).grid(column=2, row=1, padx=5, pady=5, sticky=W)
            option2 = ttk.OptionMenu(mainframe, unit2, *DistanceUnits.keys(), command = calculate).grid(column=2, row=2, padx=5, pady=5, sticky=W)
            break
        if(oper.get()=='Weight'):
            option1 = ttk.OptionMenu(mainframe, unit1, *WeightUnits.keys(), command = calculate).grid(column=2, row=1, padx=5, pady=5, sticky=W)
            option2 = ttk.OptionMenu(mainframe, unit2, *WeightUnits.keys(), command = calculate).grid(column=2, row=2, padx=5, pady=5, sticky=W)
            break
def calculate(*args):
    for i in range(0,len(Conversions)):
        if(oper.get()=='Distance'):
            try:
                calculateDistance()
                break
            except ValueError:
                pass
        if(oper.get()=='Weight'):
            try:
                calculateWeight()
                break
            except ValueError:
                pass
def calculateDistance(*args):
    DistanceFile.seek(((11*(DistanceUnits[unit1.get()]-1)))+((77*(DistanceUnits[unit2.get()]-1))))
    factor=float(DistanceFile.readline(12))
    
    try:
        value = float(userIn.get())
        userOut.set(int(factor * value * 10000000.0 + 0.5)/10000000.0)
    except ValueError:
        pass
def calculateWeight(*args):
    WeightFile.seek(((11*(WeightUnits[unit1.get()]-1)))+((77*(WeightUnits[unit2.get()]-1))))
    factor=float(WeightFile.readline(12))
    
    try:
        value = float(userIn.get())
        userOut.set(int(factor * value * 10000000.0 + 0.5)/10000000.0)
    except ValueError:
        pass

mainframe = ttk.Frame(tk, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
tk.columnconfigure(0, weight=1)
tk.rowconfigure(0, weight=1)

userIn = StringVar()
userIn_entry = ttk.Entry(mainframe, width=11, textvariable=userIn)
userIn_entry.grid(column=1, row=1, padx=5, pady=5, sticky=(W, E))

userOut = StringVar()
userOut_entry = ttk.Entry(mainframe, width=11, textvariable=userOut).grid(column=1, row=2, padx=5, pady=5, sticky=(W, E))

option3 = ttk.OptionMenu(mainframe, oper, *Conversions, command = setunits).grid(column=2, row=3, padx=5, pady=5, sticky=W)
oper.set(Conversions[0])

userIn_entry.focus()
tk.bind("<KeyPress>", calculate)

setunits()
tk.mainloop()

