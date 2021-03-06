#!/usr/bin/env python
import pika
from time import sleep
import RC_direct_controller as rc

def on_message(ch, method, properties, body):
    global pulse
    print(pulse)
    pulse = rc.changeSteer(body.decode())


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
