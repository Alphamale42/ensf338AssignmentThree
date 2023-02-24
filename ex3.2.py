import urllib
import json
import ssl
import timeit
import matplotlib.pyplot as plt
import requests

# Assignment 3, Exercise 2
 
# 1. Load the array and the list of search tasks.
context = ssl._create_unverified_context()

with urllib.request.urlopen('https://raw.githubusercontent.com/ldklab/ensf338w23/main/assignments/assignment3/ex2data.json', context=context) as url:
    array = json.load(url)

with urllib.request.urlopen('https://raw.githubusercontent.com/ldklab/ensf338w23/main/assignments/assignment3/ex2tasks.json', context=context) as tasksURL:
    tasksArray = json.load(tasksURL)

# sort the tasks array
tasksArray.sort()
print(tasksArray)

# 2. Implement a standard binary search, with the following tweak:
#    the midpoint for the first iteration must be configurable (all
#    successive iterations will just split the array in the middle).
def binarySearch(arr, low, high, key, midPoint = 0):
    if high >= low:
        if low == 0 and high == len(arr) - 1:
            mid = midPoint

        else:
            mid = (high + low) // 2 

        if arr[mid] == key:
            return mid

        elif arr[mid] > key:
            return binarySearch(arr, low, mid - 1, key)

        else:
            return binarySearch(arr, mid + 1, high, key)

    else:
        return -1

# 3. Time the performance of each search task w/ different midpoints for
#    each task. You can use whatever strategy you want to check different
#    midpoints. Then choose the best midpoint for each task.
def main():
    
    chosenMidPoints = [0, 249999, 499999, 749999, 999999]
    minTimes = []
    bestMidPoints = []
    
    for task in tasksArray:
        times = {}
        for i in chosenMidPoints:
            elapsed_time = timeit.timeit(lambda: binarySearch(array, 0, len(array) - 1, task, i), number=1)
            times[i] = elapsed_time

        for i in times.keys():
            if times[i] == min(times.values()):
                bestMidPoints.append(i)
                minTimes.append(min(times.values()))
                break


    # 4. Produce a scatterplot visualizing each task and the corresponding chosen midpoint.
    plt.scatter(tasksArray, bestMidPoints)
    plt.xlabel("Tasks")
    plt.ylabel("Initial Midpoints")
    plt.title("Tasks vs Initial Midpoints")
    plt.yticks(chosenMidPoints)
    plt.tight_layout()
    
    plt.show()


if __name__ == "__main__":
    main()
