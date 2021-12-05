import pika

from .apps import ProductsConfig

# add ampq link
params = pika.URLParameters(ProductsConfig.amqpUrl)

# create connection
connection = pika.BlockingConnection(params)

# create channel
channel = connection.channel()


def publish(body):
    # call publish
    channel.basic_publish(exchange='', routing_key='admin', body=body)
