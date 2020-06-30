# Logging over UDP in Python

this is a demo of how to use Python's [DatagramHandler](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.DatagramHandler) for logging. The DatagramHandler lets you send log messages from your code over UDP, which is a fast, lightweight internet protocol.

it requires a few things:
1. you need a UDP or "datagram" server running somewhere (to receive the messages)
2. a way to parse the incoming messages
3. Python 3.6+ (this demo uses `asyncio`)

# Usage

to run a "receiving" server:
```
python -m logging_udp
```

to log some messages to it:
```
python client_example.py
```

# FYI

* "Datagram" means a unit or chunk of data
* UDP ("user datagram protocol") is a way of sending datagrams
  * it doesn't guarantee success of delivery
    * Nerdy joke: "I'd tell you a joke about UDP, but you might not get it"
  * it doesn't guarantee order of delivery
  * but it is fast, because you don't have to wait for confirmation of delivery
* UDP can also be used to send log messages to `syslog` via the `SysLogHandler`
