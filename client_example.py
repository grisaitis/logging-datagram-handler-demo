import logging
import logging.handlers
import time


logger = logging.getLogger(__name__)
logger.setLevel("DEBUG")

udp_handler = logging.handlers.DatagramHandler("127.0.0.1", 9998)
logger.addHandler(udp_handler)

n = int(1000)
wait_s = 0.0
start = time.perf_counter()

for trial in range(n):
    # time.sleep(wait_s)
    logger.debug(f"debug message {trial}")
    logger.info(f"info message {trial}")
    logger.warning(f"warning message {trial}")
    logger.error(f"error message {trial}")
    logger.critical(f"critical message {trial}")

end = time.perf_counter()
t_per_trial = (end - start) / n - wait_s
print(f"{end - start} s total")
print(f"{n} trials")
print(f"{t_per_trial:0.8f} s per trial")
print(f"{t_per_trial * 1000:0.8f} ms per trial")

t_per_message = t_per_trial / 5
print(f"{t_per_message:0.8f} s per message")
print(f"{t_per_message * 1000:0.8f} ms per message")
