import pika

from .products.apps import ProductsConfig

params = pika.URLParameters(ProductsConfig.amqpUrl)

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')


def callback(ch, _method, _properties, body):
    print(f'[{ch}] Received: {body}')


channel.basic_consume(on_message_callback=callback, queue='admin')

print("Started Consuiming messages")

channel.start_consuming()

channel.close()
