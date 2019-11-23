import tkinter as tk
from tkinter import messagebox as msgbox
from tkinter import ttk
from functools import partial
from pcon import *
import ipaddress
import utils


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
        msgbox.showerror("Error", f'An error occured: {e}')
    else:
        # Create the new window, setting a name and the focus to the window
        t = tk.Toplevel(root)
        t.title('Active connection')
        t.focus()
        t.columnconfigure(0, weight=1)
        t.rowconfigure(0, weight=1)

        # Create a StringVar to hold the reply from the printer
        printer_reply = tk.StringVar()
        printer_reply.set('No reply received')

        # Set up the frames for buttons and labelframe
        tframe = ttk.Frame(t, padding="3 3")
        bframe = ttk.Frame(t, padding="0 3")
        # row and columnconfigure are required to get the labelframe to expand
        # to fill the available space
        tframe.columnconfigure(0, weight=1)
        tframe.rowconfigure(0, weight=1)
        tframe.grid(column=0, row=0, sticky=(tk.N, tk.E, tk.S, tk.W))
        bframe.grid(column=0, row=1, sticky=(tk.N, tk.E, tk.S, tk.W))
        # Add the printer reply labelframe. Sticky it to all sides to get it to
        # expand together with the top frame
        p_rep_frame = ttk.LabelFrame(tframe, text="Printer connection data")
        p_rep_frame.grid(column=0, row=0, columnspan=3, sticky=(tk.N, tk.E, tk.S, tk.W))

        # Create the text labels and populate the IP and Port
        ttk.Label(p_rep_frame, text="Active ip:").grid(
            column=0, row=1, sticky=tk.W)
        ttk.Label(p_rep_frame, text=p_ip).grid(column=1, row=1, padx=5, sticky=tk.W)
        ttk.Label(p_rep_frame, text="Active port:").grid(
            column=0, row=2, sticky=tk.W)
        ttk.Label(p_rep_frame, text=p_port).grid(column=1, row=2, padx=5, sticky=tk.W)

        # Create the label for the printer response
        ttk.Label(p_rep_frame, text="Printer reply:").grid(column=0, row=3, sticky=tk.W)
        ttk.Label(p_rep_frame, textvariable=printer_reply).grid(
            column=1, row=3, columnspan=2, padx=5, sticky=tk.W)

        # # Create the query button, which triggers the query function
        ttk.Button(bframe, text="Send query_con", command=partial(
            query, psock, printer_reply, b'\x04\x01\x01\xE0')).grid(column=0, row=1)

        # Create the reset button, this triggers the query function with a
        # different byte string
        ttk.Button(bframe, text="Send reset_con", command=partial(
            query, psock, printer_reply, b'\x07\x00\x01\x2c')).grid(column=1, row=1)

        ttk.Button(bframe, text="Close connection",
                   command=partial(p_sock_end, psock, t)).grid(column=2, row=1)

        # Give every child item some padding so that it doesn't look like shit.
        for child in tframe.winfo_children():
            child.grid_configure(padx=5, pady=1)

        for child in bframe.winfo_children():
            child.grid_configure(padx=5, pady=1)
