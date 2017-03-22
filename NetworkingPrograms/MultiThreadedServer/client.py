import socket               # Import socket module
import argparse
import random
from threading import Thread

def getSocket():
    s = socket.socket()         # Create a socket object
    port = 12345
    s.connect(('68.181.201.26', port))
    return s


def parseArguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--automatic", help="this mode will trigger multiple threads from client automatically")
    args = parser.parse_args()
    if args.automatic:
        print " That right ! ! ! ! !"
        return True
    return False

def triggerCommunication(sock):
    try:
        input = True
        while(input):
            user_input=str(raw_input('>Please enter string you would like capitalize : '))
            print " You have entered : ", user_input
            sock.send(user_input)
            print " Received message from server : ", sock.recv(1024)
            input = str(raw_input('>Do you want to send more message ? (Y/y/N/n/any character) : '))
            input = True if input in ['Y', 'y'] else False

        sock.send("ByeMessage")
        print sock.recv(1024)
    except:
            print "Something went wrong while connecting to server"
    finally:
            sock.close()

sample_messages = ["Hello world", "my name is deepika", "I am at ISI", " masters in cs", "expedia", "3 year work experienced", "facebook",
                   "internships", "introduction to networks", "grader", "tcp/ip protocol"];

def triggerCommunications(sock):
    #print " client running ", str(sock)
    i = 0
    while i < 3:
        index = random.randint(0, len(sample_messages)-1)
        sock.send(sample_messages[index])
        print ">Processed message : ", sock.recv(1024)
        i = i + 1

if __name__ =="__main__":
    automaticMode = parseArguments()
    sock = getSocket()

    if (not automaticMode):
        print ">Entering manual mode."
        triggerCommunication(sock)
    else:
        sockets = list()
        for i in range(5):
            sockets.append(getSocket())

        for sock in sockets:
            t = Thread(target=triggerCommunications, args=(sock,))
            t.start()
    #print " Closed"