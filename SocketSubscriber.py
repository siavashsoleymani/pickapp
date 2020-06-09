import socket
from time import sleep
import time

HOST = '127.0.0.1'
PORT = 5000
s = 1
def connect():
    global s
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))
        s.send(b'2001\n')
    except:
        print("connection lost try to reconnect")
        sleep(5)
        return connect()


connect()


def process(message):

    try:
        split = message.split(',')
        diff = int(round(time.time() * 1000)) - int(split[1])
        if diff > 200 and split[0] != ' ':
            return
        print('Received', message)
    except:
        pass


while True:
    global s

    data = s.recv(1024)
    if len(data) == 0:
        print("disconnected")
        connect()
    message = data.decode().rstrip()
    if not message.startswith('h'):
        process(message)