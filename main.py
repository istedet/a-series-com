import tkinter as TK
import tkinter.ttk as TTK
from functools import partial
from conwindow import spawnwindow


# Define a window killer functipon to close the window
def program_exit(window):
    window.destroy()

# Create the root element and set a title for the window
root = TK.Tk()
root.title('A-Series connection tool')

# Normal setup stuff to make sure that we have a frame to work in and some
# half-way decent styling.
mainframe = TTK.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(TK.N, TK.W, TK.E, TK.S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Create our two values to hold the ip and the port number:
printer_ip = TK.StringVar()
printer_port = TK.StringVar()

# Define default values
printer_ip.set('127.0.0.1')
printer_port.set('700')

# Create two text labels
TTK.Label(mainframe, text="ip address:").grid(column=0, row=0, sticky=TK.W)
TTK.Label(mainframe, text="port:").grid(column=1, row=0, sticky=TK.W)

# Create two elements to enter the IP and PORT into:
ip_entry = TTK.Entry(mainframe, width=15, textvariable=printer_ip)
ip_entry.grid(column=0, row=1, sticky=(TK.W, TK.E))

port_entry = TTK.Entry(mainframe, width=6, textvariable=printer_port)
port_entry.grid(column=1, row=1, sticky=(TK.W, TK.E))

# Create the connect button, which spawns a new window
TTK.Button(mainframe, text="Connect", command=partial(
    spawnwindow, root, printer_ip, printer_port)).grid(column=0, row=2, sticky=TK.W)

TTK.Button(mainframe, text="Exit", command=partial(
    program_exit, root)).grid(column=1, row=2, sticky=TK.W)

# Give every child item some padding so that it doesn't look like shit.
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

# Make the IP entry thingy the focus so that changing the ip is easy
ip_entry.focus()

# Start the main loop so that the program does something
root.mainloop()
