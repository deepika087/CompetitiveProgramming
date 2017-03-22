import socket               # Import socket module
from socket import *
import time
from thread import *
import traceback
#from PIL import Image

s = socket()         # Create a socket object
port = 12345                # Reserve a port for your service.
s.bind(('0.0.0.0', port))        # Bind to the port
print " Binding completed  ! !"

"""
def verify_image(fileName):
    try:
        v_image = Image.open(fileName)
        v_image.verify()
        return True
    except Exception:
        print traceback.print_exc()
        return False
"""

def clientthread(connection):
    print ">Inside function"
    fname=""
    count = 0
    messageToReturn = ""
    try:
        try:
            while True:
                if (count == 0): #Expected "NAME:<Actual Name>"
                    data = connection.recv(1024)
                    if (data):
                        data = data.split(":")
                        if (data[0] == "NAME" and data[1].isalpha()):
                            print "> Validation apss first line"
                            count += 1
                            connection.send("Received name : " + data[1])
                        else:
                            messageToReturn += "Expected format for line number 1 is NAME:<Your Name>"
                            connection.send(messageToReturn)
                    else:

                        messageToReturn += "Expected format for line number 1 is NAME:<Your Name>"
                        connection.send(messageToReturn)

                elif (count == 1): #Expected is "USC ID:<USC ID>"
                    data = connection.recv(1024)
                    print ">Second line : ", data
                    if (data):
                        data = data.split(":")
                        if (data[0] == "USC ID" and data[1].isdigit()):
                            count += 1
                            fname=str(data[1].strip() + ".jpg")
                            print "> Validation apss second line"
                            connection.send("Received USC ID : " + data[1])
                        else:
                            messageToReturn += "Expected format for line number 2 is USC ID:<Your USC Id>"
                            connection.send(messageToReturn)
                    else:
                        messageToReturn += "Expected format for line number 2 is USC ID:<Your USC Id>"
                        connection.send(messageToReturn)

                elif (count == 2):
                    if (fname == ""):
                        messageToReturn += "Something must have went wrong in the first two lines"
                        connection.send(messageToReturn)
                    else:
                        fp = open(fname,'w+')
                        print ">file name : ", fname
                        total_len=0
                        connection.settimeout(3.0)
                        try:
                            while True:
                                data = connection.recv(512)
                                total_len += len(data)
                                if(data):
                                    fp.write(data)
                                else:
                                    break
                            fp.close()
                            print ">Data received successfully"
                        except timeout:
                            print " Time out exception occured"
                            """
                            if (verify_image(fname)):
                                messageToReturn = "You have succesfully completed your assignment"
                            else:
                            """
                            messageToReturn = "You have succesfully completed your assignment"
                            connection.send(messageToReturn)
                            break;
                        break
        except Exception :
            print "> Exception occurred "
            traceback.print_exc()
    finally:
        print " Closing connection"
        connection.close()

s.listen(5)                 # Now wait for client connection.
print " Ready to accept the connections ! !"

while True:
    connection, client_address = s.accept()     # Establish connection with client.
    print ">Recieved connection from client : ", client_address
    start_new_thread(clientthread, (connection,))

s.close()
