import tkinter as tk
from tkinter import ttk
from functools import partial
from conwindow import spawnwindow


# Define a window killer functipon to close the window
def program_exit(window):
    window.destroy()


# Create the root element and set a title for the window
root = tk.Tk()
root.title('A-Series connection tool')

# Normal setup stuff to make sure that we have a frame to work in and some
# half-way decent styling.
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Create our two values to hold the ip and the port number:
printer_ip = tk.StringVar()
printer_port = tk.StringVar()

# Define default values
printer_ip.set('127.0.0.1')
printer_port.set('700')

# Create two text labels
ttk.Label(mainframe, text="ip address:").grid(column=0, row=0, sticky=tk.W)
ttk.Label(mainframe, text="port:").grid(column=1, row=0, sticky=tk.W)

# Create two elements to enter the IP and PORT into:
ip_entry = ttk.Entry(mainframe, width=15, textvariable=printer_ip)
ip_entry.grid(column=0, row=1, sticky=(tk.W, tk.E))

port_entry = ttk.Entry(mainframe, width=6, textvariable=printer_port)
port_entry.grid(column=1, row=1, sticky=(tk.W, tk.E))

# Create the connect button, which spawns a new window
ttk.Button(mainframe, text="Connect", command=partial(
    spawnwindow, root, printer_ip, printer_port)).grid(column=0, row=2, sticky=tk.W)

ttk.Button(mainframe, text="Exit", command=partial(
    program_exit, root)).grid(column=1, row=2, sticky=tk.W)

# Give every child item some padding so that it doesn't look like shit.
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

# Make the IP entry thingy the focus so that changing the ip is easy
ip_entry.focus()

# Start the main loop so that the program does something
root.mainloop()
