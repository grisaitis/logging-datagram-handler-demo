import asyncio
import logging

from .datagram_protocols import LoggingDatagramHandlerProtocol

handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter(logging.BASIC_FORMAT))

logger = logging.getLogger(__name__)
logger.setLevel("DEBUG")
logger.addHandler(handler)


def protocol_factory():
    return LoggingDatagramHandlerProtocol(logger)


async def main():
    print("Starting UDP server")
    loop = asyncio.get_running_loop()
    transport, protocol = await loop.create_datagram_endpoint(
        protocol_factory, local_addr=("127.0.0.1", 9998)
    )
    try:
        await asyncio.sleep(3600)  # Serve for 1 hour.
    finally:
        transport.close()


asyncio.run(main())
