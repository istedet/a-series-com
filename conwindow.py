import tkinter as tk
from tkinter import ttk, messagebox
from functools import partial
from pcon import *
import ipaddress


def spawnwindow(root, printer_ip, printer_port):
    # set up styles to get the correct window bakground
    style = ttk.Style()
    style.configure('textframe.TFrame', background='blue')
    style.configure('buwh.TLabel', background='blue',
                    foreground='white', font='arial 10 bold')

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
        # Create the new window, setting a name and the focus to the window
        t = tk.Toplevel(root)
        t.title('Active connection')
        t.focus()

        # Create a StringVar to hold the reply from the printer
        printer_reply = tk.StringVar()
        printer_reply.set('No reply received')

        # Create the frame in the window (I don't know if I can use "mainframe" as
        # it's already used in main.py)
        subframe = ttk.Frame(t, padding="3 3 12 12")
        subframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        itemframe = ttk.Frame(subframe, padding="3 3 12 12", borderwidth=2,
                              relief="sunken", style='textframe.TFrame')
        itemframe.grid(column=0, row=0, columnspan=3, rowspan=2, sticky=(tk.N, tk.W, tk.E, tk.S))

        t.columnconfigure(0, weight=1)
        t.rowconfigure(0, weight=1)

        # Create the text labels and populate the IP and Port
        ttk.Label(itemframe, text="Active ip:", style='buwh.TLabel').grid(
            column=1, row=1, sticky=tk.E)
        ttk.Label(itemframe, text=p_ip, style='buwh.TLabel').grid(column=2, row=1, sticky=tk.W)
        ttk.Label(itemframe, text="Active port:", style='buwh.TLabel').grid(
            column=1, row=2, sticky=tk.E)
        ttk.Label(itemframe, text=p_port, style='buwh.TLabel').grid(column=2, row=2, sticky=tk.W)

        # Create the label for the printer response
        ttk.Label(itemframe, text="Printer reply:",
                  style='buwh.TLabel').grid(column=1, row=3, sticky=tk.E)
        ttk.Label(itemframe, textvariable=printer_reply, style='buwh.TLabel').grid(
            column=2, row=3, sticky=tk.W, columnspan=2)

        # Create the query button, which triggers the query function
        ttk.Button(subframe, text="Send query_con", command=partial(
            query, psock, printer_reply, b'\x04\x01\x01\xE0')).grid(column=0, row=4)

        # Create the reset button, this triggers the query function with a
        # different byte string
        ttk.Button(subframe, text="Send reset_con", command=partial(
            query, psock, printer_reply, b'\x07\x00\x01\x2c')).grid(column=1, row=4, sticky=tk.W)

        ttk.Button(subframe, text="Close connection",
                   command=partial(p_sock_end, psock, t)).grid(column=2, row=4, sticky=tk.W)

        # Give every child item some padding so that it doesn't look like shit.
        for child in subframe.winfo_children():
            child.grid_configure(padx=5, pady=5)


# TODO: White background and black text for frame, centered text
