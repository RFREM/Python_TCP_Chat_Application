
import socket
import threading


hostname=socket.gethostname()   

def start_client():
    """Starts the client to connect to other peers"""
    # Create a TCP socket
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    while True:
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

