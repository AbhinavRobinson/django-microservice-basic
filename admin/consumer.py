import pika

params = pika.URLParameters('')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


channel.basic_consume(on_message_callback=callback, queue='admin')

print("Started Consuiming messages")

channel.start_consuming()

channel.close()
