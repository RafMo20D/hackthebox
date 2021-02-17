#!/usr/bin/env python

import pika

credentials = pika.PlainCredentials('yuntao', 'EashAnicOc3Op')
parameters = pika.ConnectionParameters('10.10.10.190',5672,'/',credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.basic_publish(exchange='', routing_key='plugin_data',
                      body=b'http://127.0.0.1:8080/hello.lua')
connection.close()
