import concurrent.futures
import logging
import queue
import random
import threading
import time


def producer(queue, event):
    while not event.is_set():
        message = random.randint(1, 101)
        logging.info("Producer got message: %s", message)
        queue.put(message)
    logging.info("Producer received event. Exiting")


def consumer(queue, event):
    while not event.is_set() or not queue.empty():
        message = queue.get()
        logging.info("Consumer storing message: %s (size=%d)", message, queue.qsize())
    logging.info("Consumer received event. Exiting")


if __name__ == "__main__":
    format_ = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format_, level=logging.INFO, datefmt="%H:%M:%S")

    pipeline = queue.Queue(maxsize=10)
    event = threading.Event()
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipeline, event)
        executor.submit(consumer, pipeline, event)

        time.sleep(0.0001)
        logging.info("Main: about to set event")
        event.set()

    # The OUTPUT:
    # 02:11:07: Producer got message: 95
    # 02:11:07: Producer got message: 20
    # 02:11:07: Producer got message: 97
    # 02:11:07: Producer got message: 44
    # 02:11:07: Producer got message: 85
    # 02:11:07: Producer got message: 47
    # 02:11:07: Producer got message: 90
    # 02:11:07: Producer got message: 51
    # 02:11:07: Producer got message: 19
    # 02:11:07: Producer got message: 32
    # 02:11:07: Producer got message: 55
    # 02:11:07: Consumer storing message: 95 (size=9)
    # 02:11:07: Consumer storing message: 20 (size=8)
    # 02:11:07: Consumer storing message: 97 (size=7)
    # 02:11:07: Consumer storing message: 44 (size=6)
    # 02:11:07: Consumer storing message: 85 (size=5)
    # 02:11:07: Consumer storing message: 47 (size=4)
    # 02:11:07: Consumer storing message: 90 (size=3)
    # 02:11:07: Consumer storing message: 51 (size=2)
    # 02:11:07: Consumer storing message: 19 (size=1)
    # 02:11:07: Consumer storing message: 32 (size=0)
    # 02:11:07: Producer got message: 55
    # 02:11:07: Producer got message: 84
    # 02:11:07: Producer got message: 47
    # 02:11:07: Producer got message: 23
    # 02:11:07: Producer got message: 34
    # 02:11:07: Producer got message: 19
    # 02:11:07: Producer got message: 88
    # 02:11:07: Producer got message: 85
    # 02:11:07: Producer got message: 69
    # 02:11:07: Producer got message: 82
    # 02:11:07: Consumer storing message: 55 (size=9)
    # 02:11:07: Consumer storing message: 55 (size=8)
    # 02:11:07: Consumer storing message: 84 (size=7)
    # 02:11:07: Consumer storing message: 47 (size=6)
    # 02:11:07: Consumer storing message: 23 (size=5)
    # 02:11:07: Consumer storing message: 34 (size=4)
    # 02:11:07: Consumer storing message: 19 (size=3)
    # 02:11:07: Consumer storing message: 88 (size=2)
    # 02:11:07: Consumer storing message: 85 (size=1)
    # 02:11:07: Consumer storing message: 69 (size=0)
    # 02:11:07: Main: about to set event
    # 02:11:07: Producer received event. Exiting
    # 02:11:07: Consumer storing message: 82 (size=0)
    # 02:11:07: Consumer received event. Exiting
