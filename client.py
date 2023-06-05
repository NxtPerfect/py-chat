import socket
import sys


def run_client():
    IP_ADDRESS = sys.argv[1]
    PORT = int(sys.argv[2])
    # bytes(sys.argv[3])

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # send message
        s.connect((IP_ADDRESS, PORT))
        s.sendall(b"msg")
        data = s.recv(1024)
    print(f'Message {data!r}')


if __name__ == "__main__":
    run_client()
