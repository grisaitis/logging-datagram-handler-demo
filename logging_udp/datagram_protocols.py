import asyncio
import logging

from .making_log_record import make_log_record
from logging_udp.types import Address


class LoggingDatagramHandlerProtocol(asyncio.DatagramProtocol):
    def __init__(self, logger: logging.Logger):
        super().__init__()
        self.logger = logger

    def datagram_received(self, data: bytes, addr: Address):
        log_record = make_log_record(data)
        self.logger.handle(log_record)


class StringProtocol(asyncio.DatagramProtocol):
    def datagram_received(self, data: bytes, addr: Address):
        print(data.decode('utf-8'))


class JsonProtocol(asyncio.DatagramProtocol):
    def datagram_received(self, data: bytes, addr: Address):
        import json
        json_obs = json.loads(data, encoding='utf-8')
        print(json_obs.dumps(indent=2, sort_keys=True))
