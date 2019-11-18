from tkinter import *
from tkinter import ttk
from functools import partial
from conwindow import spawnwindow

# Create the root element and set a title for the window
root = Tk()
root.title('A-Series connection tool')

# Normal setup stuff to make sure that we have a frame to work in and some
# half-way decent styling.
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Create our two values to hold the ip and the port number:
printer_ip = StringVar()
printer_port = StringVar()

# Define default values
printer_ip.set('192.168.1.92')
printer_port.set('700')

# Create two text labels
ttk.Label(mainframe, text="ip address:").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="port:").grid(column=2, row=1, sticky=W)

# Create two elements to enter the IP and PORT into:
ip_entry = ttk.Entry(mainframe, width=20, textvariable=printer_ip)
ip_entry.grid(column=1, row=2, sticky=(W, E))

port_entry = ttk.Entry(mainframe, width=6, textvariable=printer_port)
port_entry.grid(column=2, row=2, sticky=(W, E))

# Create the connect button, which spawns a new window
ttk.Button(mainframe, text="connect", command=partial(
    spawnwindow, root, printer_ip, printer_port)).grid(column=3, row=2, sticky=E)

# Give every child item some padding so that it doesn't look like shit.
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

# Make the IP entry thingy the focus so that changing the ip is easy
ip_entry.focus()

# Start the main loop so that the program does something
root.mainloop()
