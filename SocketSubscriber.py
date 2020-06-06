import socket
from time import sleep

HOST = '127.0.0.1'
PORT = 5000

def connect():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))
        s.send(b'2001\n')
        return s
    except:
        print("connection lost try to reconnect")
        sleep(5)
        return connect()


s = connect()
while True:
    data = s.recv(1024)
    if len(data) == 0:
        print("disconnected")
        connect()
    print('Received', data.decode().rstrip())