
from re import X
import socket
import threading
import subprocess

subprocess.call('start python Python_TCP_Chat_Application_Client.py', shell=True)
subprocess.call('start python Python_TCP_Chat_Application_Client_2.py', shell=True)

hostname=socket.gethostname()   
IPAddrGET=socket.gethostbyname(hostname) 

ServerName = (hostname)
SERVER_ADDR = (IPAddrGET, 4545)

clientCount = 1


def start_server():

    # Create a TCP socket

    global server_sock
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the server's address and port
    server_sock.bind(SERVER_ADDR)

    # Listen for incoming connections
    server_sock.listen()
   
    print (f'\n-----------------------------')
    print (f'       SERVER STARTED')
    print (f' ')
    print (f'Server Host Name: {hostname}')
    print (f'Server Address: {IPAddrGET}')
    print (f'Server Address Port: 4545')
    print (f'Server Status: LISTENING')
    print (f'------------------------------')

    while True:

        clientCount + 1
    
        # Accept incoming connections
        global conn, addr
        conn, addr = server_sock.accept()

        # Add the client to the list of connected clients
        clients.append((clientCount, addr))

        # Start a new thread to handle the client connection
        client_thread = threading.Thread(target=handle_client, args=(conn, addr))
        client_thread.start()

        # Add the client thread to the list
        client_threads.append(client_thread)

        print('-------CLIENT CONNECTED-------')


def handle_client(conn, addr):

    while True:
        # Receive data from the client
        data = conn.recv(1024)
        if not data:
            break

        # Process the data
        message = data.decode()
        print(f'CLIENT {addr} SENT MESSAGE: {message}')

    # Close the connection
    conn.close()
    print(f'Closed connection with {addr}')

def displayHelp():

     print ("*-HELP SELECTED-*")
     print ("Option 2 - Display IP Adress: Shows the IP Address of this process")
     print ("Option 3 - Display Port Number: Shows the port number of this process")
     print ("Option 4 - Display Connections: Shows list of connected clients")
     print ("Option 5 - Terminates a given connection")
     print ("Option 6 - Send Message to Host IP: Send message to the server selected")
     print ("Option 7 - EXIT / QUIT: Exit this process")   

     mainMenu()

def displayConnections():

    for x in range(len(clients)):
        print (clients[x])

    mainMenu()

def sendMessage():
        message = input('Enter message: ')
        conn.sendall(message.encode())

def displayIp():

    print (server_sock)

    mainMenu()

def displayPort():

    print (server_sock)

    mainMenu()

def termConnection():

    # Remove the client from the list of connected clients
    print("---CLIENTS CONNECTED---")
    for x in range(len(clients)):
        print (clients[x])
    print("------------------------")

    # Remove the client from the list of connected clients
    clients.remove((conn, addr))

    # Close the connection
    conn.close()
    print(f'Closed connection with {addr}')
    
    mainMenu()


def mainMenu():
    print (f'---------MENU OPTIONS---------')
    print ("1.HELP"           )
    print ("2.DISPLAY IP ADDRESS"          )
    print ("3.DISPLAY PORT NUMBER"        )
    print ("4.DISPLAY CONNECTIONS" )
    print ("5.TERMINATE CONNECTION")
    print ("6.SEND MESSAGE"        )
    print ("7.EXIT / QUIT"           )
    print (f'------------------------------')

    choice=int(input())
    
    #help Display information about the available user interface options or command manual.  
    if choice==1:
       displayHelp()
    #myip Display the IP address of this process.
    elif choice==2:
        displayIp()
    #myport Display the port on which this process is listening for incoming connections. 
    elif choice==3:
        displayPort()
    #list Display a numbered list of all the connections this process is part of
    elif choice==4:
        displayConnections()
    #terminate  <connection  id.>  This  command  will  terminate  the  connection  listed  under  the  specified number  when  LIST  is  used  to  display  all  connections.  E.g.,  terminate  2. 
    elif choice==5:
        termConnection()
    #send  <connection id.>  <message>  (For example, send 3 Oh! This project is a piece of cake). This will send the message to the host on the connection
    elif choice==6:
        sendMessage()
    else:
    #exit Close all connections and terminate this process. 
        server_sock.close()

if __name__ == '__main__':

    # Create a list to store all client threads
    client_threads = []

    # Create a list to store all connected clients
    clients = []
   
    # Start the server and client on separate threads
    server_thread = threading.Thread(target=start_server)
    server_thread.start()

    #client_thread = threading.Thread(target=start_client)
    #client_thread.start()

    # Wait for all client threads to complete
    for client_thread in client_threads:
        client_thread.join()

    mainMenu()

