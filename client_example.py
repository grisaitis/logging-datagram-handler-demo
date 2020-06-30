import logging
import logging.handlers
import time


logger = logging.getLogger(__name__)

udp_handler = logging.handlers.DatagramHandler("127.0.0.1", 9998)

logger.addHandler(udp_handler)

n = int(1e4)
t = time.perf_counter()
wait_s = 0.0

for _ in range(n):
    # time.sleep(wait_s)
    # logger.debug("debug message")
    # logger.info("info message")
    # logger.warning("warning message")
    # logger.error("error message")
    logger.critical("critical message")

t = time.perf_counter() - t - n * wait_s
t_per_trial = t / n
print(f"{n} trials")
print(f"{t_per_trial:0.8f} s per trial")
print(f"{t_per_trial * 1000:0.8f} ms per trial")
