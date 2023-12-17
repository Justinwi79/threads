"""
Name: Harold Justin Windham
Date: 11/20/2022
Assignment: Module 13: Using Threads with Locks
Due Date: 11/20/2022
About this project: Threads that display list of integers
Assumptions: N/A
All work below was performed by Harold Justin Windham
"""

"""
References: Dr. Works modules and course videos. 
"""

import random
import time
import threading
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s', )


def producer(e): # producer function to generate random ints
    while (True):
        time.sleep(4)
        count = random.randint(1, 100000)
        print(f'The current maximum of all the values is ={count}')
        e.set()


def consumer(e):  # consumer function to justify max threads
    while (True):
        e.wait()
        print("Max Thread: ", max(producer(e)))
        e.clear()


def main():  # running threads
    e = threading.Event()
    # e = 1
    t1 = threading.Thread(name='',
                          target=consumer,
                          args=[e])

    t2 = threading.Thread(name='',
                          target=producer,
                          args=[e])
    t1.start()
    t2.start()

    t1.join()
    t2.join()


if __name__ == '__main__':
    main()

"""
/Users/justinwindham/PycharmProjects/threads/venv/bin/python /Users/justinwindham/PycharmProjects/threads/lock.py
The current maximum of all the values is =88986
The current maximum of all the values is =20231
The current maximum of all the values is =32171
The current maximum of all the values is =38728
The current maximum of all the values is =15177
Traceback (most recent call last):
  File "/Users/justinwindham/PycharmProjects/threads/lock.py", line 57, in <module>
    main()
  File "/Users/justinwindham/PycharmProjects/threads/lock.py", line 52, in main
    t1.join()
  File "/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/threading.py", line 1011, in join
    self._wait_for_tstate_lock()
  File "/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/threading.py", line 1027, in _wait_for_tstate_lock
    elif lock.acquire(block, timeout):
KeyboardInterrupt
The current maximum of all the values is =78047
The current maximum of all the values is =67569

Process finished with exit code 137 (interrupted by signal 9: SIGKILL)
"""