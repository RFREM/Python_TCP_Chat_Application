
import socket
import threading

hostname=socket.gethostname() 
IPAddrGET=socket.gethostbyname(hostname) 

def start_client():
    # Create a TCP socket

    global client_sock 
    client_sock= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #while True:

    #    global conn, addr
    #    conn, addr = client_sock.accept()

    #    # Start a new thread to handle the servver connection
    #    server_thread = threading.Thread(target=handle_server, args=(conn, addr))
    #    server_thread.start()

#def handle_server(conn, addr):
#    """Handles incoming client connections"""
#    while True:
#        # Receive data from the client
#        data = conn.recv(1024)
#        if not data:
#            break

#        # Process the data
#        message = data.decode()
#        print(f'CLIENT {addr} SENT MESSAGE: {message}')

#    # Close the connection
#    conn.close()
#    print(f'Closed connection with {addr}')


def connectToIp():

    global peer_addr
    peer_addr = input('Enter Server Address: ')

    global peer_port
    peer_port = input('Enter Server Port: ')

    global SERVER_ADDR2
    SERVER_ADDR2 = (peer_addr, int(peer_port))

     # Connect to the peer

    client_sock.connect((peer_addr, int(peer_port)))

    print (f'-----------------------------')
    print (f'      SERVER CONNECTED')
    print (f'------------------------------')

    mainMenu()

    return SERVER_ADDR2

def sendMessagetoIp():

    msg = input('Enter message: ')
    # Send the message to the peer
    client_sock.sendall(msg.encode())

    #print = ("Send message from server?")
    #print = ("1. YES")
    #print = ("2. NO")

    #mesgFromServ = input('Enter Choice: ')

    #if mesgFromServ == 1:

    #    response = client_sock.recv(1024)
    #    print(f'SERVER {SERVER_ADDR2} SENT MESSAGE: {response.decode()}')

    #else:
    mainMenu()

def decodeMessage():

    response = client_sock.recv(1024)
    print(f'SERVER {SERVER_ADDR2} SENT MESSAGE: {response.decode()}')

def displayHelp():

     print ("*-HELP SELECTED-*")
     print ("Option 2 - Display IP Adress: Shows the IP Address of this process")
     print ("Option 3 - Display Port Number: Shows the port number of this process")
     print ("Option 4 - Connect to IP: Connect to IP Address of server")
     print ("Option 5 - Send Message to Host IP: Send message to the server selected")
     print ("Option 6 - EXIT / QUIT: Exit this process")   

     mainMenu()

def displayIp():

    print (client_sock)

    mainMenu()

def displayPort():

    print (client_sock)

    mainMenu()


def mainMenu():

    print (f'--------C2 MENU OPTIONS--------')
    print ("1.HELP"           )
    print ("2.DISPLAY IP ADDRESS"          )
    print ("3.DISPLAY PORT NUMBER"        )
    print ("4.CONNECT TO IP" )
    print ("5.SEND MESSAGE TO HOST IP"        )
    print ("6.EXIT / QUIT"           )
    print (f'------------------------------')

    choice=int(input())
    
    #help Display information about the available user interface options or command manual.  
    if choice==1:
        displayHelp()
    #myip Display the IP address of this process.
    elif choice==2:
        print ("*-DISPLAY MACHINE IP ADDRESS-*")
        displayIp()
    #myport Display the port on which this process is listening for incoming connections. 
    elif choice==3:
        print ("*-DISPLAY MACHINE PORT-*")
        displayPort()
    #list Display a numbered list of all the connections this process is part of
    elif choice==4:
        print ("*-CONNECT TO IP SELECTED-*")
        connectToIp()
    #terminate  <connection  id.>  This  command  will  terminate  the  connection  listed  under  the  specified number  when  LIST  is  used  to  display  all  connections.  E.g.,  terminate  2. 
    elif choice==5:
        print ("*-SEND MESSAGE SELECTED-*")
        sendMessagetoIp()
    #send  <connection id.>  <message>  (For example, send 3 Oh! This project is a piece of cake). This will send the message to the host on the connection
    else:
        #exit Close all connections and terminate this process. 
        client_sock.close()

    return choice

if __name__ == '__main__':

    client_thread = threading.Thread(target=start_client)
    client_thread.start()

    mainMenu()

