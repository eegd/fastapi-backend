import json
import logging

import pika
import pika.delivery_mode

from fastapi import status
from fastapi.responses import JSONResponse

from app.amqp.amqp_factory import AmqpFactory
from app.model.request_model import TaskCreate
from app.utility.config import GlobalConfig


class ProducerService:
    logger = logging.Logger(__name__)
    amqp = AmqpFactory()
    _cfg = GlobalConfig()

    def __init__(self) -> None:
        self.exchange_name = self._cfg.EXCHANGE_NAME
        self.routing_key = self._cfg.ROUTING_KEY
        self.channel = self.amqp.create_channel()

    def create_publish(
        self,
        payload: TaskCreate,
    ):
        try:
            self.logger.warning(f"[create_publish] {payload}")
            self.channel.basic_publish(
                exchange=self.exchange_name,
                routing_key=self.routing_key,
                body=json.dumps({"key": payload.key, "msg": payload.msg}),
                properties=pika.BasicProperties(
                    delivery_mode=pika.DeliveryMode.Persistent
                ),
            )
        except Exception as err:
            self.logger.error(f"[create_publish] {err}")
            return JSONResponse(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content="Internal Server Error",
            )
