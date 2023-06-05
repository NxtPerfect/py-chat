import socket
import sys

"""Create a Socket:

    Create a socket using the socket.socket() function, specifying the socket type and address family (typically socket.AF_INET for IPv4).
    Bind the socket to a specific IP address and port using the bind() method.

Listen for Connections:

    Use the listen() method to start listening for incoming connections on the specified IP address and port.
    Accept incoming connections using the accept() method, which will return a new socket for each incoming connection.

Manage Multiple Connections:

    Use the select module to handle multiple connections simultaneously.
    Create a list to store the active sockets, including the main server socket and any connected client sockets.
    Use the select() function to monitor the sockets for any readable data or new connections.

Handle Client Connections:

    When a new connection is accepted, create a new thread or a separate process to handle the communication with the client.
    Within each thread/process, you can use the client socket to send and receive messages.

Broadcast Messages:

    Maintain a list of active client sockets to keep track of connected clients.
    Whenever a message is received from one client, iterate through the list of client sockets and send the message to each connected client (except the sender).

Clean Up:

    Properly close all the sockets and release any acquired resources when the chat room is being shut down."""


def run_server():
    if len(sys.argv) < 3:
        print("Not enough arguments, pass in script, ip address, port")
        exit()

    IP_ADDRESS = sys.argv[1]
    PORT = int(sys.argv[2])

    print(f'{IP_ADDRESS}, {PORT}')

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((IP_ADDRESS, PORT))
        s.listen(5)
        clientsocket, address = s.accept()
        with clientsocket:
            print(f'Success! Connected to {address}')
            while True:
                msg = clientsocket.recv(1024)
                if not msg:
                    break
                clientsocket.sendall(msg)


if __name__ == "__main__":
    run_server()
