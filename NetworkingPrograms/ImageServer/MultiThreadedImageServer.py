
import socket               # Import socket module
import time
from thread import *

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.
s.bind(('0.0.0.0', port))        # Bind to the port
print " Binding completed  ! !"

def clientthread(connection):
    fname="myfile.png"
    fp = open(fname,'w+')
    total_len = 0
    while True:
        data = connection.recv(512)
        total_len += len(data)
        if(data):
            fp.write(data)
        else:
            break
    fp.close()
    print "> Length of data : ", total_len
    print ">Data received successfully"
    connection.close()

s.listen(5)                 # Now wait for client connection.
print " Ready to accept the connections ! !"

while True:
    connection, client_address = s.accept()     # Establish connection with client.
    print ">Recieved connection from client : ", client_address
    start_new_thread(clientthread, (connection,))

connection.close()
s.close()
