import socket               # Import socket module

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)         # Create a socket object
port = 12345                # Reserve a port for your service.
s.bind(('0.0.0.0', port))        # Bind to the port
print " Binding completed  ! !"

def handleData(client_data, socket, client_address):

    print ">Length = ", len(client_data), " size = ", len("deepika".encode("utf-8"))
    if (client_data.startswith("Name:")):
        client_data = client_data.split(":")[1]
        if (client_data.isalpha()):
            socket.sendo("Received Name:" + client_data.strip(), client_address)
        else:
            socket.sendto("Expected format is Name:<your name>", client_address)
    elif (client_data.startswith("USC ID:")):
        client_data = unicode(client_data.split(":")[1], 'utf-8')
        if (client_data.isnumeric()):
            socket.sendto("Received USC ID:" + client_data.strip(), client_address)
        else:
            socket.sendto("Expected format is USC ID:<your id>", client_address)
    else:
        fp = open("my_new_rose.png", 'w+')
        fp.write(client_data)
        fp.close()
        socket.sendto("Image received successfully.", client_address)

print " Ready to accept the connections ! !"

while True:
    d = s.recvfrom(65536)
    client_data = d[0]
    client_address = d[1]     # Establish connection with client.
    print ">Received connection from client : ", client_address
    handleData(client_data, s, client_address)

s.close()
