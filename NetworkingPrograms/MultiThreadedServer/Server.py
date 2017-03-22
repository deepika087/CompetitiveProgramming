

import socket               # Import socket module
import time
from thread import *

def clientthread(connection, client_address):
    while True:
        data = connection.recv(1024)
        if(data):
            if (data == "ByeMessage"):
                connection.send("Thank you for using our services ! !")
                break;
            else:
                print "> Sending data to client to client : " , str(client_address)
                connection.send(data.upper())


s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.
s.bind(('0.0.0.0', port))        # Bind to the port
print " Binding completed  ! !"

s.listen(5)                 # Now wait for client connection.
print " Ready to accept the connections ! !"

while True:
    connection, client_address = s.accept()     # Establish connection with client.
    #client_address.settimeout(60)
    start_new_thread(clientthread, (connection,client_address))

connection.close()
s.close()
