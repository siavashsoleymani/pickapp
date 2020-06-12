import socket
from time import sleep
import time
import RC_speed_controller as rc_speed
import RC_direct_controller as rc_direct

HOST = 'snapptix.ir'
PORT = 8081
s = 1


def connect():
    global s
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))
        s.send(b'2001\n')
    except:
        print('connection lost try to reconnect')
        sleep(5)
        return connect()


connect()


def process(message):
    try:
        split = message.split(',')
        diff = int(round(time.time() * 1000)) - int(split[1])
        command = split[0]
        if diff > 200 and command != ' ':
            print('WARNING LATENCY IS MORE THAN 200 MILLIS')
            return
        # print('Received', message)
        if command == 'a' or command == 'd' or command == 'f':
            rc_direct.changeSteer(command)
        elif command == 'w' or command == 's' or command == ' ':
            rc_speed.control(command)

    except:
        pass


while True:
    # try:
    #     pass
    # except:
    #     connect()
    data = s.recv(1024)
    if len(data) == 0:
        print('disconnected')
        connect()
    message = data.decode().rstrip()
    if not message.startswith('h'):
        process(message)
