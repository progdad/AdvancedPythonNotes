from concurrent.futures import ThreadPoolExecutor
import logging
import threading
import time

format_ = "%(asctime)s: %(message)s"
logging.basicConfig(format=format_, level=logging.INFO, datefmt="%H:%M:%S")


def thread_function(name):
    logging.info(f"Thread {name}: starting")
    time.sleep(2)
    logging.info(f"Thread {name}: middle")
    time.sleep(1)
    logging.info(f"Thread {name}: finishing")


def threading_method():
    threads = []
    for index in range(5):
        thread = threading.Thread(target=thread_function, args=(f"({index}, {1})",))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


def no_join_method():
    with ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(thread_function, range(5))


if __name__ == '__main__':
    threading_method()
    no_join_method()

    # Example OUTPUT(it's always different):
        # 15:44:15: Thread (0, 1): starting
        # 15:44:15: Thread (1, 1): starting
        # 15:44:15: Thread (2, 1): starting
        # 15:44:15: Thread (3, 1): starting
        # 15:44:15: Thread (4, 1): starting
        # 15:44:17: Thread (4, 1): middle
        # 15:44:17: Thread (2, 1): middle
        # 15:44:17: Thread (3, 1): middle
        # 15:44:17: Thread (0, 1): middle
        # 15:44:17: Thread (1, 1): middle
        # 15:44:18: Thread (4, 1): finishing
        # 15:44:18: Thread (0, 1): finishing
        # 15:44:18: Thread (3, 1): finishing
        # 15:44:18: Thread (1, 1): finishing
        # 15:44:18: Thread (2, 1): finishing
        # 15:44:18: Thread 0: starting
        # 15:44:18: Thread 1: starting
        # 15:44:18: Thread 2: starting
        # 15:44:18: Thread 3: starting
        # 15:44:18: Thread 4: starting
        # 15:44:20: Thread 0: middle
        # 15:44:20: Thread 1: middle
        # 15:44:20: Thread 3: middle
        # 15:44:20: Thread 2: middle
        # 15:44:20: Thread 4: middle
        # 15:44:21: Thread 0: finishing
        # 15:44:21: Thread 1: finishing
        # 15:44:21: Thread 3: finishing
        # 15:44:21: Thread 2: finishing
        # 15:44:21: Thread 4: finishing
