# write your code here
import socket
import sys
import bruteforce

def establish_connection(ip, port):
    with socket.socket() as conn:
        address = (ip, int(port))  # port to int cause of int is required
        conn.connect(address)
        func = bruteforce.guess_password()
        while True:
            message = next(func)
            conn.send(str(message).encode())
            response = conn.recv(1024)
            if(response.decode()) == "Connection success!":
                print(message)
                break


def main():
    establish_connection(sys.argv[1], sys.argv[2])


if __name__ == "__main__":
    main()
