
import socket               # Import socket module
import time

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.
s.bind(('localhost', port))        # Bind to the port
print " Binding completed  ! !"

s.listen(5)                 # Now wait for client connection.
print " Ready to accept the connections ! !"

try:
    connection, client_address = s.accept()     # Establish connection with client.
except:
    print " Something went wrong in accepting conenction "

if (connection):
    while True:
        data = connection.recv(1024)
        if (data):
            print " Data received from client : ", str(data)
            print " Sending data back to client : ", data.upper()
            connection.send(data.upper())
