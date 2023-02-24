import threading
import random
import time

class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None for i in range(size)]
        self.head = self.tail = -1
        self._lock = threading.Lock()

    def lock(self):
        self._lock.acquire()

    def unlock(self):
        self._lock.release()

    # 3.    Complete the queue. The queue should use an array of predetermined size as
    #       circular buffer as seen in class and the labs. The queue should behave as follow:
    
    # a.    When enqueue() is called, the function should call lock(), insert an element
    #       (or do nothing if the queue is full), and call unlock(). If an element was
    #       inserted, the function should return. If the queue was full, the function should
    #       wait one second and try again.
    def enqueue(self, data):
        self.lock()
        # check if queue is full
        if (self.tail + 1) % self.size == self.head:
            self.unlock()
            time.sleep(1)
            self.enqueue(data)
        # else, add data to queue
        else:
            if self.head == -1:
                self.head = 0
            self.tail = (self.tail + 1) % self.size
            self.queue[self.tail] = data

            self.unlock()
            return

    # b.    When dequeue() is called, the function should call lock(), remove an
    #       element (or do nothing if the queue is empty), and call unlock(). If an element
    #       was retrieved, it should be returned. If the queue was empty, the function
    #       should wait one second and try again.
    def dequeue(self):
        self.lock()
        # check if queue is empty
        if self.head == -1:
            self.unlock()
            time.sleep(1)
            return self.dequeue()
        # if queue is not empty, remove data from queue
        else:
            data = self.queue[self.head]
            self.queue[self.head] = None
            if self.head == self.tail:
                self.head = -1
                self.tail = -1
            else:
                self.head = (self.head + 1) % self.size

            self.unlock()
            return data

# 1.    Complete the producer thread. The producer thread should randomly generate a
#       number between 1 and 10, wait that many seconds, and then enqueue the number to
#       the queue. It should do this in a loop which never terminates.
def producer():
    while True:
        randomNumber = random.randint(1, 10)
        time.sleep(randomNumber)
        q.enqueue(randomNumber)

# 2.    Complete the consumer thread. The consumer thread should randomly generate a
#       number between 1 and 10, wait that many seconds, and then dequeue a number from
#       the queue and print it to terminal.
def consumer():
    while True:
        randomNumber = random.randint(1, 10)
        time.sleep(randomNumber)
        print(q.dequeue())

if __name__ == '__main__':
    q = CircularQueue(5)
    t1 = threading.Thread(target=producer)
    t2 = threading.Thread(target=consumer)
    t1.start()
    t2.start()
    t1.join()
    t2.join()