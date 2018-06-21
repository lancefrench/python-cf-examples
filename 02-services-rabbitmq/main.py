from flask import Flask
import os
import sys
import pika
import json

app = Flask(__name__)

port = int(os.getenv("PORT"))


@app.route('/')
def hello_rabbit():
    vcap_services = json.loads(os.getenv('VCAP_SERVICES'))
    amqp_url = vcap_services['p-rabbitmq'][0]['credentials']['protocols']['amqp']['uri']
    return 'AMQP URL: ' + str(amqp_url)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)