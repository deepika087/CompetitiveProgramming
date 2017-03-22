__author__ = 'deepika'

import traceback
import socket               # Import socket module
import argparse

def getSocket(ipAddress, portNum):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)         # Create a socket object
    s.connect((ipAddress, int(portNum)))
    return s

def parseArguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", help="Server's ip address will go here")
    parser.add_argument("-p", help="Server's port number will go here")
    parser.add_argument("-i", help="Image's file name will go here")
    parser.add_argument("-l", help="Log file name will go here")
    args = parser.parse_args()
    return args.a, args.p, args.i, args.l

if __name__ =="__main__":
    ipAddress, portNum, fileName, logfilename = parseArguments()
    sock = getSocket(ipAddress, portNum)
    try:

        buffer = "NAME:Deepika"
        sock.send(buffer)
        data = sock.recv(1024)
        print "> Message from Server=>",str(data)

        buffer = "USC ID:0123456789"
        sock.send(buffer)
        data = sock.recv(1024)
        print "> Message from Server=>",str(data)

        buffer = ""
        buffer += open(fileName, 'rb').read()

        sock.send(buffer)
        data = sock.recv(1024)
        print "> Message from Server=>",str(data)
    except Exception :
        print " Some exception occured"
        traceback.print_exc()
    finally:

        sock.close()

