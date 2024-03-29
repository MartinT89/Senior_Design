import socket
import sys
from _thread import *
import threading

print_lock = threading.Lock()


def threaded(c):
    while True:

        data = c.recv(1024)
        if not data:
            print('Bye')
            sys.exit(0)
        message = str(data.decode('ascii'))

        if message[0] == "1":
            message = "Received speed(mph) rate: " + message.replace("1:", '')

        if message[0] == "2":
            message = "Received hydration level(SpO2) rate: " + message.replace("2:", '')

        if message[0] == "3":
            message = "Received heart rate(BPM) rate: " + message.replace("3:", '')

        print(message)
        c.send(message.encode('ascii'))

    c.close()


def Main():
    try:
        host = ""
        port = 12345
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((host, port))
        print("socket binded to port", port)

        s.listen(5)
        print("socket is listening")

        while True:
            c, addr = s.accept()

            print('Connected to :', addr[0], ':', addr[1])

            start_new_thread(threaded, (c,))
        s.close()
    except KeyboardInterrupt as msg:
        sys.exit(0)


if __name__ == '__main__':
    Main()
