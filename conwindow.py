from tkinter import *
from tkinter import ttk, messagebox
from functools import partial
from pcon import *
import ipaddress


def spawnwindow(root, printer_ip, printer_port):

    try:
        # Retrieve the values from the previous window as this one is created
        p_ip = printer_ip.get()
        p_port = int(printer_port.get())

        # Check the ip-adress. Raises an exception if it isn't a valid ip-address
        ipaddress.ip_address(p_ip)

        # Create your socket
        psock = p_connect(p_ip, p_port)

    except Exception as e:
        messagebox.showinfo("Error", f'An error occured: {e}')
    else:
        # Create the new window
        t = Toplevel(root)

        # Create a StringVar to hold the reply from the printer
        printer_reply = StringVar()
        printer_reply.set('No reply received yet')

        # Create the frame in the window (I don't know if I can use "mainframe" as
        # it's already used in main.py)
        subframe = ttk.Frame(t, padding="3 3 12 12")
        subframe.grid(column=0, row=0, sticky=(N, W, E, S))
        t.columnconfigure(0, weight=1)
        t.rowconfigure(0, weight=1)

        # Create the text labels and populate the IP and Port
        ttk.Label(subframe, text="Active ip:").grid(column=1, row=1, sticky=E)
        ttk.Label(subframe, text=p_ip).grid(column=2, row=1, sticky=W)
        ttk.Label(subframe, text="Active port:").grid(column=1, row=2, sticky=E)
        ttk.Label(subframe, text=p_port).grid(column=2, row=2, sticky=W)

        # Create the label for the printer response
        ttk.Label(subframe, text="Printer reply:").grid(column=1, row=3, sticky=E)
        ttk.Label(subframe, textvariable=printer_reply).grid(column=2, row=3, sticky=W)

        # Create the query button, which triggers the query function
        ttk.Button(subframe, text="Query connections", command=partial(
            query, psock, printer_reply, b'\x04\x01\x01\xE0')).grid(column=1, row=4, sticky=E)

        # Create the reset button, this triggers the query function with a
        # different byte string
        ttk.Button(subframe, text="Reset connections", command=partial(
            query, psock, printer_reply, b'\x07\x00\x01\x2c')).grid(column=2, row=4, sticky=W)

        # Give every child item some padding so that it doesn't look like shit.
        for child in subframe.winfo_children():
            child.grid_configure(padx=5, pady=5)
