import threading

lock = threading.Lock()
print("before first acquire")
lock.acquire()
print("before second acquire")
# The program is being frozen here because a Lock instance
# is supposed to be .release() before another .acquire() running
lock.acquire()
print("acquired lock twice")


# To solve this issue we need to be used RLock class
lock1 = threading.RLock()
print("before first acquire")
lock1.acquire()
print("before second acquire")
lock1.acquire()
print("acquired lock twice")
lock1.release()
lock1.release()
