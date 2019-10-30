
import random
import socket
import time


def Main():
    host = '127.0.0.1'

    port = 12345

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect((host, port))

    while True:
        message = "2:" + str(random.randrange(8, 30))
        s.send(message.encode('ascii'))

        data = s.recv(1024)

        print('Received from the server :', str(data.decode('ascii')))
        time.sleep(10)
    # close the connection



if __name__ == '__main__':
    Main()