import pika
import logging
from config import init_log_config


connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
chanel = connection.channel()

chanel.queue_declare(queue="test_queue")

init_log_config(logging.INFO)
log = logging.getLogger(__name__)


def callback(channel, method, properties, body):
    # Декодируем тело сообщения
    message = body.decode()
    log.info(f" [x] Received message: {message}")

    # Выводим метаданные доставки
    log.info(f" [x] Exchange: {method.exchange}")
    log.info(f" [x] Routing key: {method.routing_key}")
    log.info(f" [x] Delivery tag: {method.delivery_tag}")
    log.info(f" [x] Redelivered: {method.redelivered}")

    # Выводим свойства сообщения
    log.info(f" [x] Content type: {properties.content_type}")
    log.info(f" [x] Delivery mode: {properties.delivery_mode}")
    log.info(f" [x] Headers: {properties.headers}")
    log.info(f" [x] Correlation ID: {properties.correlation_id}")

    log.info("----------------------------------------------------------------")

    chanel.basic_ack(delivery_tag=method.delivery_tag)


chanel.basic_consume(queue="test_queue", on_message_callback=callback, auto_ack=False)

chanel.start_consuming()
