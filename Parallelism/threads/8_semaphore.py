import logging
from concurrent.futures import ThreadPoolExecutor
from threading import *
import time


def display(semaphore, num):
    semaphore_dict = semaphore.__dict__
    logging.info(f"Thread-{num} BEFORE ACQUIRE, semaphore count is {semaphore_dict['_value']}")
    semaphore.acquire()
    for i in range(2):
        logging.info(f"Thread-{num} before sleep")
        time.sleep(1)
        semaphore.release()
        logging.info(f"Thread-{num} AFTER RELEASE, semaphore count is {semaphore_dict['_value']}")


if __name__ == '__main__':
    format_ = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format_, level=logging.DEBUG, datefmt="%H:%M:%S")

    semaphore = Semaphore(3)

    with ThreadPoolExecutor(max_workers=4) as executor:
        four_semaphores = (semaphore for _ in range(4))
        executor.map(display, four_semaphores, range(1, 5))

    # The OUTPUT:
    # 21:15:07: Thread-1 BEFORE ACQUIRE, semaphore count is 3
    # 21:15:07: Thread-1 before sleep
    # 21:15:07: Thread-2 BEFORE ACQUIRE, semaphore count is 2
    # 21:15:07: Thread-2 before sleep
    # 21:15:07: Thread-3 BEFORE ACQUIRE, semaphore count is 1
    # 21:15:07: Thread-3 before sleep
    # 21:15:07: Thread-4 BEFORE ACQUIRE, semaphore count is 0
    # 21:15:08: Thread-1 AFTER RELEASE, semaphore count is 1
    # 21:15:08: Thread-1 before sleep
    # 21:15:08: Thread-4 before sleep
    # 21:15:08: Thread-2 AFTER RELEASE, semaphore count is 1
    # 21:15:08: Thread-2 before sleep
    # 21:15:08: Thread-3 AFTER RELEASE, semaphore count is 2
    # 21:15:08: Thread-3 before sleep
    # 21:15:09: Thread-4 AFTER RELEASE, semaphore count is 3
    # 21:15:09: Thread-4 before sleep
    # 21:15:09: Thread-1 AFTER RELEASE, semaphore count is 4
    # 21:15:09: Thread-2 AFTER RELEASE, semaphore count is 5
    # 21:15:09: Thread-3 AFTER RELEASE, semaphore count is 6
    # 21:15:10: Thread-4 AFTER RELEASE, semaphore count is 7
