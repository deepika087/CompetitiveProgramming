import socket               # Import socket module

def getSocket():
    s = socket.socket()         # Create a socket object
    #host = socket.gethostname() # Get local machine name
    port = 12345
    s.connect(('68.181.201.26', port))
    return s

if __name__ == "__main__":
    sock = getSocket()
    try:
        print " You will have your chance to send the data. Let me show you a demo first. "
        sock.send("This is the message.  It will be capitalized ! !");
        print "Received message from server : ", sock.recv(1024)

        input = True
        while(input):
            user_input=str(raw_input('>Please enter string you would like capitalize : '))
            print " You have entered : ", user_input
            sock.send(user_input)
            print " Received message from server : ", sock.recv(1024)
            input = str(raw_input('>Do you want to send more message ? (Y/y/N/n/any character) : '))
            input = True if input in ['Y', 'y'] else False
    except:
        print "Something went wrong while connecting to server"
    finally:
        sock.close()





