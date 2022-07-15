# write your code here
import socket
import sys


def establish_connection(ip, port, message):
    with socket.socket() as conn:
        address = (ip, int(port))  # port to int cause of int is required
        conn.connect(address)
        conn.send(message.encode())
        response = conn.recv(1024)

        print(response.decode())


def main():
    establish_connection(sys.argv[1], sys.argv[2], sys.argv[3])


if __name__ == "__main__":
    main()
