
import socket
import threading

hostname=socket.gethostname()   
IPAddrGET=socket.gethostbyname(hostname) 

ServerName = (hostname)
SERVER_ADDR = (IPAddrGET, 4545)

def start_server():
    """Starts the server to listen for incoming connections"""
    # Create a TCP socket
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the server's address and port
    server_sock.bind(SERVER_ADDR)

    # Listen for incoming connections
    server_sock.listen()
   
    print (f'-----------------------------')
    print (f'       SERVER STARTED')
    print (f' ')
    print (f'Server Host Name: {hostname}')
    print (f'Server Address: {IPAddrGET}')
    print (f'Server Address Port: 4545')
    print (f'Server Status: LISTENING')
    print (f'------------------------------')

    while True:
        # Accept incoming connections
        conn, addr = server_sock.accept()

        # Add the client to the list of connected clients
        clients.append((conn, addr))

        # Start a new thread to handle the client connection
        client_thread = threading.Thread(target=handle_client, args=(conn, addr))
        client_thread.start()

        # Add the client thread to the list
        client_threads.append(client_thread)

        print('-------CLIENT CONNECTED-------')

def handle_client(conn, addr):
    """Handles incoming client connections"""
    while True:
        # Receive data from the client
        data = conn.recv(1024)
        if not data:
            break

        # Process the data
        message = data.decode()
        print(f'CLIENT {addr} SENT MESSAGE: {message}')

        #Sends Messafe
        message = input('Enter message: ')
        sendMessage(message, conn)

        # Send the message to all connected clients except the sender
        for client_conn, client_addr in clients:
            if client_addr != addr:
                client_conn.sendall(message.encode())
           # Prompt the user to enter a message

    # Remove the client from the list of connected clients
    clients.remove((conn, addr))

    # Close the connection
    conn.close()
    print(f'Closed connection with {addr}')

def sendMessage(message, sock):
   
    sock.sendall(message.encode())

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
