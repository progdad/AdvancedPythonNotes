import threading

l = threading.Lock()
print("before first acquire")
l.acquire()
print("before second acquire")
# The program is being frozen here because a Lock instance
# is supposed to be .release() before another .acquire() running
l.acquire()
print("acquired lock twice")


# To solve this issue it needs to be used RLock class
l1 = threading.RLock()
print("before first acquire")
l1.acquire()
print("before second acquire")
l1.acquire()
print("acquired lock twice")
l1.release()
l1.release()
