import pika

# add ampq link
params = pika.URLParameters('')

# create connection
connection = pika.BlockingConnection(params)

# create channel
channel = connection.channel()


def publish(_method, body: dict):
    # call publish
    channel.basic_publish(exchange='', routing_key='admin', body=body)
