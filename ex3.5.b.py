import timeit
import matplotlib.pyplot as plt

H = [10000000]*10000000
size = -1
   
# Function to return the index of the
# parent node of a given node
def parent(i) :
 
    return (i - 1) // 2
   
# Function to return the index of the
# left child of the given node
def leftChild(i) :
 
    return ((2 * i) + 1)
   
# Function to return the index of the
# right child of the given node
def rightChild(i) :
 
    return ((2 * i) + 2)
     
# Function to shift up the 
# node in order to maintain 
# the heap property
def shiftUp(i) :
 
    while (i > 0 and H[parent(i)] < H[i]) :
           
        # Swap parent and current node
        swap(parent(i), i)
       
        # Update i to parent of i
        i = parent(i)
         
# Function to shift down the node in
# order to maintain the heap property
def shiftDown(i) :
 
    maxIndex = i
       
    # Left Child
    l = leftChild(i)
       
    if (l <= size and H[l] > H[maxIndex]) :
     
        maxIndex = l
       
    # Right Child
    r = rightChild(i)
       
    if (r <= size and H[r] > H[maxIndex]) :
     
        maxIndex = r
       
    # If i not same as maxIndex
    if (i != maxIndex) :
     
        swap(i, maxIndex)
        shiftDown(maxIndex)
         
# Function to insert a 
# new element in 
# the Binary Heap
def insert(p) :
     
    global size
    size = size + 1
    H[size] = p
       
    # Shift Up to maintain 
    # heap property
    shiftUp(size)
   
# Function to extract 
# the element with
# maximum priority
def extractMax() :
     
    global size
    result = H[0]
       
    # Replace the value 
    # at the root with 
    # the last leaf
    H[0] = H[size]
    size = size - 1
       
    # Shift down the replaced 
    # element to maintain the 
    # heap property
    shiftDown(0)
    return result
   
# Function to change the priority
# of an element
def changePriority(i,p) :
 
    oldp = H[i]
    H[i] = p
       
    if (p > oldp) :
     
        shiftUp(i)
  
    else :
     
        shiftDown(i)
   
# Function to get value of 
# the current maximum element
def getMax() :
  
    return H[0]
   
# Function to remove the element
# located at given index
def Remove(i) :
 
    H[i] = getMax() + 1
       
    # Shift the node to the root
    # of the heap
    shiftUp(i)
       
    # Extract the node
    extractMax()
   
def swap(i, j) :
     
    temp = H[i]
    H[i] = H[j]
    H[j] = temp
     
# Insert the element to the
# priority queue
insert(45)
insert(20)
insert(14)
insert(12)
insert(31)
insert(7)
insert(11)
insert(13)
insert(7)
i = 0
# Priority queue before extracting max
print("Priority Queue : ", end = "")
while (i <= size) :
    print(H[i], end = " ")
    i += 1
print()
# Node with maximum priority
print("Node with maximum priority :" ,  extractMax())
# Priority queue after extracting max
print("Priority queue after extracting maximum : ", end = "")
j = 0
while (j <= size) :
    print(H[j], end = " ")
    j += 1
print()
# Change the priority of element
# present at index 2 to 49
changePriority(2, 49)
print("Priority queue after priority change : ", end = "")
k = 0
while (k <= size) :
 
    print(H[k], end = " ")
    k += 1
print()
# Remove element at index 3
Remove(3)
print("Priority queue after removing the element : ", end = "")
l = 0
while (l <= size) :
    print(H[l], end = " ")
    l += 1

list_times2 = []
for iter in range(100):
    for j in range(1000):
        time_elapsed = timeit.timeit(lambda: insert(j), number=1)
    list_times2.append(time_elapsed)
# plt.plot(list_times2)
# plt.ylabel('times')
# plt.xlabel('iteration number')
# plt.show()

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



# plt.plot(list_times)
# plt.ylabel('times')
# plt.xlabel('iteration number')
# plt.show()

#plot list_times2 and list_times on the same graph

plt.plot(list_times2, label='Binary Heap')
plt.plot(list_times, label='Priority Queue')
plt.ylabel('times')
plt.xlabel('iteration number')
plt.legend()
plt.show()