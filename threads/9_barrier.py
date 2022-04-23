import logging
import time
from concurrent.futures import ThreadPoolExecutor
from threading import Barrier


barrier = Barrier(2)


def barrier_function(value, tt_sleep):
    for _ in range(2):
        logging.info(f"Thread {value} before sleep")
        time.sleep(tt_sleep)
        logging.info(f"Thread {value} is waiting on barrier, waiting barriers = {barrier.n_waiting}")
        barrier.wait()
        logging.info(f"Thread {value} was released")
    logging.info(f"Thread {value} is done")


if __name__ == '__main__':
    format_ = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format_, level=logging.DEBUG, datefmt="%H:%M:%S")

    tt_sleep = [1, 2, 3]
    with ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(barrier_function, range(1, 4), tt_sleep)

    # The OUTPUT:
    # 15:43:33: Thread 1 before sleep
    # 15:43:33: Thread 2 before sleep
    # 15:43:33: Thread 3 before sleep
    # 15:43:34: Thread 1 is waiting on barrier, waiting barriers = 0
    # 15:43:35: Thread 2 is waiting on barrier, waiting barriers = 1
    # 15:43:35: Thread 2 was released
    # 15:43:35: Thread 2 before sleep
    # 15:43:35: Thread 1 was released
    # 15:43:35: Thread 1 before sleep
    # 15:43:36: Thread 3 is waiting on barrier, waiting barriers = 0
    # 15:43:36: Thread 1 is waiting on barrier, waiting barriers = 1
    # 15:43:36: Thread 1 was released
    # 15:43:36: Thread 1 is done
    # 15:43:36: Thread 3 was released
    # 15:43:36: Thread 3 before sleep
    # 15:43:37: Thread 2 is waiting on barrier, waiting barriers = 0
    # 15:43:39: Thread 3 is waiting on barrier, waiting barriers = 1
    # 15:43:39: Thread 3 was released
    # 15:43:39: Thread 3 is done
    # 15:43:39: Thread 2 was released
    # 15:43:39: Thread 2 is done
