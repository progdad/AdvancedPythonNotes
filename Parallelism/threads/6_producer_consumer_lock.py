import logging
import random
import threading
from concurrent.futures import ThreadPoolExecutor


class Pipeline:
    def __init__(self):
        self.message = 0
        self.producer_lock = threading.Lock()
        self.consumer_lock = threading.Lock()
        self.consumer_lock.acquire()

    def get_message(self, name):
        logging.debug("%s:about to acquire getlock", name)
        self.consumer_lock.acquire()
        logging.debug("%s:have getlock", name)
        message = self.message
        logging.debug("%s:about to release setlock", name)
        self.producer_lock.release()
        logging.debug("%s:setlock released", name)
        return message

    def set_message(self, message, name):
        logging.debug("%s:about to acquire setlock", name)
        self.producer_lock.acquire()
        logging.debug("%s:have setlock", name)
        self.message = message
        logging.debug("%s:about to release getlock", name)
        self.consumer_lock.release()
        logging.debug("%s:getlock released", name)


SENTINEL = object()


def producer(pipeline):
    for index in range(5):
        message = random.randint(1, 101)
        logging.info("Producer got message: %s", message)
        pipeline.set_message(message, "Producer")

    # Send a sentinel message to tell consumer we're done
    pipeline.set_message(SENTINEL, "Producer")


def consumer(pipeline):
    message = 0
    while message is not SENTINEL:
        message = pipeline.get_message("Consumer")
        if message is not SENTINEL:
            logging.info("Consumer storing message: %s", message)


if __name__ == "__main__":
    format_ = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format_, level=logging.DEBUG, datefmt="%H:%M:%S")

    pipeline = Pipeline()
    with ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipeline)
        executor.submit(consumer, pipeline)

    # The OUTPUT:
    # 21:06:11: Producer got message: 74
    # 21:06:11: Producer:about to acquire setlock
    # 21:06:11: Producer:have setlock
    # 21:06:11: Producer:about to release getlock
    # 21:06:11: Producer:getlock released
    # 21:06:11: Producer got message: 97
    # 21:06:11: Producer:about to acquire setlock
    # 21:06:11: Consumer:about to acquire getlock
    # 21:06:11: Consumer:have getlock
    # 21:06:11: Consumer:about to release setlock
    # 21:06:11: Consumer:setlock released
    # 21:06:11: Consumer storing message: 74
    # 21:06:11: Consumer:about to acquire getlock
    # 21:06:11: Producer:have setlock
    # 21:06:11: Producer:about to release getlock
    # 21:06:11: Producer:getlock released
    # 21:06:11: Producer got message: 22
    # 21:06:11: Producer:about to acquire setlock
    # 21:06:11: Consumer:have getlock
    # 21:06:11: Consumer:about to release setlock
    # 21:06:11: Consumer:setlock released
    # 21:06:11: Consumer storing message: 97
    # 21:06:11: Consumer:about to acquire getlock
    # 21:06:11: Producer:have setlock
    # 21:06:11: Producer:about to release getlock
    # 21:06:11: Producer:getlock released
    # 21:06:11: Producer got message: 58
    # 21:06:11: Producer:about to acquire setlock
    # 21:06:11: Consumer:have getlock
    # 21:06:11: Consumer:about to release setlock
    # 21:06:11: Consumer:setlock released
    # 21:06:11: Consumer storing message: 22
    # 21:06:11: Consumer:about to acquire getlock
    # 21:06:11: Producer:have setlock
    # 21:06:11: Producer:about to release getlock
    # 21:06:11: Producer:getlock released
    # 21:06:11: Producer got message: 15
    # 21:06:11: Producer:about to acquire setlock
    # 21:06:11: Consumer:have getlock
    # 21:06:11: Consumer:about to release setlock
    # 21:06:11: Consumer:setlock released
    # 21:06:11: Consumer storing message: 58
    # 21:06:11: Consumer:about to acquire getlock
    # 21:06:11: Producer:have setlock
    # 21:06:11: Producer:about to release getlock
    # 21:06:11: Producer:getlock released
    # 21:06:11: Producer:about to acquire setlock
    # 21:06:11: Consumer:have getlock
    # 21:06:11: Consumer:about to release setlock
    # 21:06:11: Consumer:setlock released
    # 21:06:11: Consumer storing message: 15
    # 21:06:11: Consumer:about to acquire getlock
    # 21:06:11: Producer:have setlock
    # 21:06:11: Producer:about to release getlock
    # 21:06:11: Producer:getlock released
    # 21:06:11: Consumer:have getlock
    # 21:06:11: Consumer:about to release setlock
    # 21:06:11: Consumer:setlock released
