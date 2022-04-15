import logging
import threading
import time


def thread_function(name):
    logging.info(f"Thread {name}: starting")
    time.sleep(2)
    logging.info(f"Thread {name}: finishing")


if __name__ == "__main__":
    format_ = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format_, level=logging.INFO, datefmt="%H:%M:%S")

    logging.info("Main : before creating thread")
    thread = threading.Thread(target=thread_function, args=(1,))#, daemon=True)
    # "daemon" makes a thread as a backgroung thread
    logging.info("Main : before running thread")
    thread.start()
    logging.info("Main : wait for the thread to finish")
    #thread.join()
    # .join() is a method that runs a "thread" until its completed, whether if it's a daemon thread or it's not
    logging.info("Main : all done")


# The OUTPUT of non daemon thread without .join() method:
    # 17: 53:19: Main: before creating thread
    # 17: 53:19: Main: before running thread
    # 17: 53:19: Thread 1: starting
    # 17: 53:19: Main: wait for the thread to finish
    # 17: 53:19: Main: all done
    # 17: 53:21: Thread 1: finishing

# The OUTPUT of an any thread with .join() method :
    # 18:19:03: Main : before creating thread
    # 18:19:03: Main : before running thread
    # 18:19:03: Thread 1: starting
    # 18:19:03: Main : wait for the thread to finish
    # 18:19:05: Thread 1: finishing
    # 18:19:05: Main : all done

# The OUTPUT of a daemon thread:
    # 18:36:22: Main : before creating thread
    # 18:36:22: Main : before running thread
    # 18:36:22: Thread 1: starting
    # 18:36:22: Main : wait for the thread to finish
    # 18:36:22: Main : all done


# The explanation of the code are here >>> https://realpython.com/intro-to-python-threading/
