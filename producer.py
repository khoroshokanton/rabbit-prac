import pika
import logging

log = logging.getLogger(__name__)

try:
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    chanel = connection.channel()

    chanel.queue_declare(queue="test_queue")

    for i in range(10):
        log.info("Отправляем сообщение %d", i)

        chanel.basic_publish(
            exchange="",
            routing_key="test_queue",
            body=f"Hello, RabbitMQ! {i}",
        )

except Exception as e:
    log.error("Ошибка отправки сообщения в очередь %e", e, exc_info=True)

finally:
    connection.close()
