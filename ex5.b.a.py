
'''
Code below is an inefficient way of implementing a priority queue
for the reason that the time complexity for deletion is O(n).

A more effecient way of implementing a priority queue is by making use
of the binary heap data structure which is in the other file in the repo.

With a binary heap, the time complexity for deletion is O(log(n)).

'''

import timeit
import matplotlib.pyplot as plt
class PriorityQueue(object):
    def __init__(self):
        self.queue = []
 
    def __str__(self):
        return ' '.join([str(i) for i in self.queue])
 
    # for checking if the queue is empty
    def isEmpty(self):
        return len(self.queue) == 0
 
    # for inserting an element in the queue
    def insert(self, data):
        self.queue.append(data)
 
    # for popping an element based on Priority
    def delete(self):
        try:
            max_val = 0
            for i in range(len(self.queue)):
                if self.queue[i] > self.queue[max_val]:
                    max_val = i
            item = self.queue[max_val]
            del self.queue[max_val]
            return item
        except IndexError:
            print()
            exit()
if __name__ == '__main__':
    myQueue = PriorityQueue()
    myQueue.insert(12)
    myQueue.insert(1)
    myQueue.insert(14)
    myQueue.insert(7)
    myQueue.delete()
    print(myQueue)           
    while not myQueue.isEmpty():
        print(myQueue.delete())
myobj = PriorityQueue()
list_times = []
for iter in range(100):
    for i in range(1000):
        time_elapsed = timeit.timeit(lambda: myobj.insert(i), number=1)
    list_times.append(time_elapsed)
plt.plot(list_times)
plt.ylabel('times')
plt.xlabel('iteration number')
plt.show()
