# 3. a. Search in a sorted array (produce code ex3.5.a.py)

import timeit
import matplotlib.pyplot as plt

# Create a sorted list with 1000 elements
array = []
for i in range(0, 1000):
    array.append(i)

# Efficient method: Binary Search
# Worst case complexity: O(log n)
def binarySearch(arr, low, high, key):
    if high >= low:
        mid = (high + low) // 2 

        if arr[mid] == key:
            return mid

        elif arr[mid] > key:
            return binarySearch(arr, low, mid - 1, key)

        else:
            return binarySearch(arr, mid + 1, high, key)

    else:
        return -1
    
#Inefficient method: Linear Search
# Worst case complexity: O(n)
def linearSearch(arr, n, key):
    for i in range(0, n):
        if arr[i] == key:
            return i
    return -1

def main():
    # Provide the code for an experiment that demonstrates the difference. The experiment should: 
    # (i) time the execution of both implementations on realistic, large inputs (1000 elements or above); 
    # (ii) plot the distribution of measured values across multiple measurements (>= 100 measurements per task); and 
    # (iii) print an aggregate of the measured values (min or average as appropriate).

    # (i) time the execution of both implementations on realistic, large inputs (1000 elements or above);
    binaryTimes = []
    linearTimes = []
    for task in array:
        elapsed_time_binary = timeit.timeit(lambda: binarySearch(array, 0, len(array) - 1, task), number=100)
        binaryTimes.append(elapsed_time_binary)
        
        elapsed_time_linear = timeit.timeit(lambda: linearSearch(array, len(array), task), number=100)
        linearTimes.append(elapsed_time_linear)

    # (ii) plot the distribution of measured values across multiple measurements (>= 100 measurements per task);
    plt.plot(array, binaryTimes)
    plt.plot(array, linearTimes)
    plt.xlabel('Tasks')
    plt.ylabel('Elapsed Time')
    plt.title('Binary Search vs. Linear Search')
    plt.legend(['Binary Search', 'Linear Search'])
    plt.tight_layout()
    plt.show()

    # (iii) print an aggregate of the measured values (min or average as appropriate).
    print("Binary Search Avg Elapsed Time:", sum(binaryTimes) / len(binaryTimes))
    print("Linear Search Avg Elapsed Time:", sum(linearTimes) / len(linearTimes))

if __name__ == '__main__':
    main()
