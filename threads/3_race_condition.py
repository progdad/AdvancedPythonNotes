import logging
from concurrent.futures import ThreadPoolExecutor
import time


class FakeDatabase:
    def __init__(self):
        self.value = 0

    def update(self, name):
        logging.info("Thread %s: starting update", name)
        local_copy = self.value
        local_copy += 1
        time.sleep(0.1)
        self.value = local_copy
        logging.info("Thread %s: finishing update", name)


if __name__ == "__main__":
    format_ = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format_, level=logging.INFO, datefmt="%H:%M:%S")

    database = FakeDatabase()
    logging.info("Testing update. Starting value is %d.", database.value)
    with ThreadPoolExecutor(max_workers=2) as executor:
        for index in range(2):
            executor.submit(database.update, index)
    logging.info("Testing update. Ending value is %d.", database.value)

    # The OUTPUT:d
        # 15:59:36: Testing update. Starting value is 0.
        # 15:59:36: Thread 0: starting update
        # 15:59:36: Thread 1: starting update
        # 15:59:37: Thread 0: finishing update
        # 15:59:37: Thread 1: finishing update
        # 15:59:37: Testing update. Ending value is 1.

# The solution of how to make the code work without a race condition is in "4_lock_synchronization.py" file
