from concurrent.futures import ThreadPoolExecutor
import logging
import threading
import time


class FakeDatabase:
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()

    def locked_update(self, name):
        logging.info("Thread %s: starting update", name)
        logging.debug("Thread %s about to lock", name)
        with self._lock:
            logging.debug("Thread %s has lock", name)
            local_copy = self.value
            local_copy += 1
            time.sleep(0.1)
            self.value = local_copy
            logging.debug("Thread %s about to release lock", name)
        logging.debug("Thread %s after release", name)
        logging.info("Thread %s: finishing update", name)


if __name__ == '__main__':
    format_ = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format_, level=logging.DEBUG, datefmt="%H:%M:%S")

    database = FakeDatabase()
    logging.info("Testing update. Starting value is %d.", database.value)
    with ThreadPoolExecutor(max_workers=2) as executor:
        for index in range(2):
            executor.submit(database.locked_update, index)
    logging.info("Testing update. Ending value is %d.", database.value)

    # Now there is no race condition anymore
    # The OUTPUT:
        # 17:57:15: Testing update. Starting value is 0.
        # 17:57:15: Thread 0: starting update
        # 17:57:15: Thread 0 about to lock
        # 17:57:15: Thread 0 has lock
        # 17:57:15: Thread 1: starting update
        # 17:57:15: Thread 1 about to lock
        # 17:57:15: Thread 0 about to release lock
        # 17:57:15: Thread 0 after release
        # 17:57:15: Thread 0: finishing update
        # 17:57:15: Thread 1 has lock
        # 17:57:15: Thread 1 about to release lock
        # 17:57:15: Thread 1 after release
        # 17:57:15: Thread 1: finishing update
        # 17:57:15: Testing update. Ending value is 2.
    