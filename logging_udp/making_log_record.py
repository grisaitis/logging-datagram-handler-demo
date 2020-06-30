import logging
from logging import LogRecord
import pickle
import struct

# logger = logging.getLogger(__name__)


def make_log_record(data: bytes) -> LogRecord:
    # logger.info("making LogRecord from datagram packet")
    # logger.debug(f"datagram packet is {len(data)} bytes long")
    slen = struct.unpack(">L", data[0:4])[0]
    # logger.debug(f"LogRecord pickle is {slen} bytes long")
    log_record_pickle = data[4:]
    if len(log_record_pickle) != slen:
        raise RuntimeError("Datagram packet incomplete")
    obj = pickle.loads(log_record_pickle)
    return logging.makeLogRecord(obj)
