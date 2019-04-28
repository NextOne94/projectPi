from tkinter import *
from tkinter import ttk
import socket
root = Tk()
root.geometry("400x400")
# Initialize our country "databases":
#  - the list of country codes (a subset anyway)
#  - a parallel list of country names, in the same order as the country codes
#  - a hash table mapping country code to population<
drungname = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', \
             'V', 'W', 'X')

dnames = StringVar(value=drungname)
datatoserver = []
text = StringVar(root, value='1')

host = '192.168.137.165'
port = 5000
s = socket.socket()
s.connect((host, port))


def sendData(*args):
    print("AAA")
    # datatoserver.clear()
    datatoservernew ="-"
    for i in range(0, len(datatoserver), 1):
        datatoserverold = str(datatoserver[i])+'-'
        datatoservernew = datatoservernew + datatoserverold

    s.send(datatoservernew.encode('utf-8'))

    print(datatoservernew)
    lbox2.delete(0, lbox2.size())
    datatoserver.clear()


def selectDrug(*args):
    print("BBB")
    idxs = lbox1.curselection()

    idx = int(idxs[0])
    lbox1.see(idx)
    name = drungname[idx]
    datatoserver.append(idx)
    num = lbox2.size()
    lbox2.insert(num, name)

    for i2 in range(0,lbox2.size(),2):
        lbox2.itemconfigure(i2, background='#f0f0ff')



def clearData(*args):
    print("CCC")
    lbox2.delete(0, lbox2.size())
    datatoserver.clear()


# Create and grid the outer content frame
c = ttk.Frame(root, padding=(12, 0, 12, 12))
c.grid(column=0, row=0, sticky=(N,W,E,S))
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0,weight=1)

# Create the different widgets; note the variables that many
# of them are bound to, as well as the button callback.
# Note we're using the StringVar() 'cnames', constructed from 'countrynames'
lbox1 = Listbox(c, listvariable=dnames, height=5)
lbox2 = Listbox(c, height=5)
lbl = ttk.Label(c, text="Drug List ")
lb2 = ttk.Label(c, text="Amount : ")
lb3 = ttk.Label(c, text="selected drugs ")
lb4 = ttk.Label(c, text="Amount ")
select = ttk.Button(c, text='Select', command=selectDrug, default='active')
clear = ttk.Button(c, text='clear', command=clearData, default='active')
send = ttk.Button(c, text='SendData', command=sendData,default='active')
entry1 = ttk.Entry(c, width=5, textvariable=text)

# Grid all the widgets
lbox1.grid(column=0, row=1, rowspan=4, columnspan=4, sticky=(N,S,E,W))
lbl.grid(column=0, row=0, sticky=W)
lb2.grid(column=4, row=1, sticky=W)
entry1.grid(column=5, row=1, columnspan=1, sticky=W)
select.grid(column=5, row=3, sticky=W)
clear.grid(column=5, row=4, sticky=W)
lb3.grid(column=0, row=5, sticky=W)
lb4.grid(column=2, row=5, sticky=W)
lbox2.grid(column=0, row=6, rowspan=2, columnspan=4, sticky=(N,S,E,W))
send.grid(column=5, row=7, sticky=W)
c.grid_columnconfigure(0, weight=1)
c.grid_rowconfigure(6, weight=1)

# Set event bindings for when the selection in the listbox changes,
# when the user double clicks the list, and when they hit the Return key


# Colorize alternating lines of the listbox
for i in range(0,len(drungname),2):
    lbox1.itemconfigure(i, background='#f0f0ff')


# Set the starting state of the interface, including selecting the
# default gift to send, and clearing the messages.  Select the first
# country in the list; because the <<ListboxSelect>> event is only
# generated when the user makes a change, we explicitly call showPopulation.

lbox1.selection_set(0)


root.mainloop()