__author__ = 'deepika'


import socket               # Import socket module
import argparse
import random
from threading import Thread

def getSocket():
    s = socket.socket()         # Create a socket object
    port = 12345
    s.connect(('localhost', port))
    return s

if __name__ =="__main__":
    sock = getSocket()
    try:
        img = open('myshot.png','rb')
        buffer = ""
        while True:
            strng = img.readline(512)
            if not strng:
                break
            sock.send(strng)
        print "Data sent successfully"
    except Exception as e:
        print " Some exception occured", e.message, e
    finally:
        img.close()
        sock.close()