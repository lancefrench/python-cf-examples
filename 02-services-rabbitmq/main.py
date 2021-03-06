from flask import Flask
import os
import pika
import json

app = Flask(__name__)

port = int(os.getenv("PORT"))


@app.route('/')
def hello_rabbit():
    vcap_services = json.loads(os.getenv('VCAP_SERVICES'))
    amqp_url = vcap_services['p-rabbitmq'][0]['credentials']['protocols']['amqp']['uri']

    # Publish
    connection = pika.BlockingConnection(pika.URLParameters(amqp_url))
    channel = connection.channel()
    channel.queue_declare(queue='hello')
    channel.basic_publish(exchange='',
                          routing_key='hello',
                          body='Hello World!')
    connection.close()

    # Consume
    connection = pika.BlockingConnection(pika.URLParameters(amqp_url))
    channel = connection.channel()
    channel.queue_declare('hello')
    method_frame, header_frame, body = channel.basic_get(queue='hello', no_ack=False)
    if method_frame:
        channel.basic_ack(method_frame.delivery_tag)

    return 'AMQP URL: ' + str(amqp_url)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)