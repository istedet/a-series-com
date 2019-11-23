import socket
import select
from tkinter import messagebox as msgbox


# Connect creates the socket and returns it so it's accessible for other
# functions
def p_connect(p_ip, p_port):
    # Create the socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the IP/Port
    s.connect((p_ip, p_port))

    # Return the socket so the other functions can use it.
    return s


# Query takes three arguments (in order), the socket variable, a StringVar to
# store the reply in and a byte string to send to the printer
def query(s, dispvalue, p_command):
    # Catch a connection error from host going offline after connection was
    # accepted
    try:
        # Send the query
        s.sendall(p_command)

        # use select to see if there is any data coming from the printer.
        # if we receive data within 5 s we print it, if not we print an error.
        ready = select.select([s], [], [], 5)

        # Set the display value to the received byte stream if you get a reply
        # in time. If not, set a timeout message
        if ready[0]:
            data = s.recv(1024)
            dispvalue.set(repr(data)[2:-1])
        else:
            dispvalue.set('Response timeout (5s)')
    except Exception as e:
        msgbox.showerror("Error", f'An error occured: {e}')


# Function to end the connection
def p_sock_end(s, t):
    # Shut down the socket, close the socket and kill the window
    s.shutdown(socket.SHUT_RDWR)
    s.close()

    t.destroy()
