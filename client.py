import socket
import sys
import select

from _thread import *


def run_client():
    IP_ADDRESS = str(sys.argv[1])
    PORT = int(sys.argv[2])

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if len(sys.argv) < 3:
        print("Not enough arguments, pass in script, ip address, port")
        exit()
    server.connect((IP_ADDRESS, PORT))

    sockets_list = [sys.stdin, server]

    read_sockets, write_sockets, error_sockets = select.select(
        sockets_list, [], [])

    while True:
        for socks in read_sockets:
            if socks == server:
                message = server.recv(2048)
                print(message)
            else:
                msg = bytes(sys.stdin.readline(), 'utf-8')
                server.send(msg)
                sys.stdout.write("< You >: ")
                sys.stdout.write(str(msg).strip("b\'\"\\n\""))
                sys.stdout.write("\n")
                sys.stdout.flush()
    server.close()


if __name__ == "__main__":
    run_client()
