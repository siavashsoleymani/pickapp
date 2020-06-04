#!/usr/bin/env python
import pika
import sys
from time import sleep
import Adafruit_PCA9685

pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(50)
pulse = 300
servo_mid = 300
step_min = 4
servo_min = 210
servo_max = 390
pwm.set_pwm(5, 0, pulse)
pwm.set_pwm(7, 0, pulse)
print(' [*] Waiting for logs. To exit press CTRL+C')

def changeSteer(arrow):
    global pulse
    if arrow == 'd' :
        pulse += step_min
        if pulse >= servo_max:
            pulse = pulse - step_min
        pwm.set_pwm(5, 0, pulse)
        pwm.set_pwm(7, 0, pulse)
    elif arrow == 'a':
        pulse -= step_min
        if pulse <= servo_min:
            pulse = pulse + step_min
        pwm.set_pwm(5, 0, pulse)
        pwm.set_pwm(7, 0, pulse)
    elif arrow == 'f' :
        pulse = servo_mid
        pwm.set_pwm(5, 0, pulse)
        pwm.set_pwm(7, 0, pulse)
    return pulse



def on_message(ch, method, properties, body):
    global pulse
    print(pulse)
    pulse = changeSteer(body.decode())


while True:
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='snapptix.ir'))
        channel = connection.channel()
        result = channel.queue_declare(queue='', exclusive=True)
        queue_name = result.method.queue
        channel.queue_bind(exchange='pickapp-exchange', queue=queue_name, routing_key="pickapp-direct-routingkey")
        channel.basic_consume(queue=queue_name, on_message_callback=on_message, auto_ack=True)
        channel.start_consuming()
    except:
        print("connection lost")
        sleep(1)
        continue

    connection.close()
    break
