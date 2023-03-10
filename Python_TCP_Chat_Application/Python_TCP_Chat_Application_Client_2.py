
import socket
import threading

hostname=socket.gethostname() 
IPAddrGET=socket.gethostbyname(hostname) 

def mainMenu():

    print (f'---------MENU OPTIONS---------')
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
        print (f'-----------------------------')
        print (f'      SERVER CONNECTED')
        print (f'Client Name: {hostname}')
        print (f'Client Address: {IPAddrGET}')
        print (f'------------------------------')
    #myip Display the IP address of this process.
    elif choice==2:
        option2()
    #myport Display the port on which this process is listening for incoming connections. 
    elif choice==3:
        option3()
    #list Display a numbered list of all the connections this process is part of
    elif choice==4:
        option4()
    #terminate  <connection  id.>  This  command  will  terminate  the  connection  listed  under  the  specified number  when  LIST  is  used  to  display  all  connections.  E.g.,  terminate  2. 
    elif choice==5:
        option5()
    #send  <connection id.>  <message>  (For example, send 3 Oh! This project is a piece of cake). This will send the message to the host on the connection
    elif choice==6:
        option6()
    else:
    #exit Close all connections and terminate this process. 
        option7()

    return choice

def start_client():
    """Starts the client to connect to other peers"""
    # Create a TCP socket
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)



    while True:

        menuChoice = mainMenu()

        # Get the peer's address and port from the user

        peer_addr = input('Enter Server Address: ')
        peer_port = input('Enter Server Port: ')

        SERVER_ADDR2 = (peer_addr, int(peer_port))

        # Connect to the peer
        client_sock.connect((peer_addr, int(peer_port)))
        print (f'-----------------------------')
        print (f'      SERVER CONNECTED')
        print (f'Client Name: {hostname}')
        print (f'Client Address: {peer_addr}')
        print (f'------------------------------')

        while True:

            # Prompt the user to enter a message
            msg = input('Enter message: ')

            # Send the message to the peer
            client_sock.sendall(msg.encode())

            # Receive messages from the peer
            response = client_sock.recv(1024)
            print(f'SERVER {SERVER_ADDR2} SENT MESSAGE: {response.decode()}')

            # If the user entered "/quit", exit the loop
            if msg == '/quit':
                break

        # Close the connection
        client_sock.close()
        break

if __name__ == '__main__':

    ## Start the server and client on separate threads
    #server_thread = threading.Thread(target=start_server)
    #server_thread.start()

    client_thread = threading.Thread(target=start_client)
    client_thread.start()

