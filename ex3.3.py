import sys

# 2.    Produce test code (ex3.3.py) that checks the correctness of your inference for lists up to
#       64 elements. Specifically, write a Python loop that grows a list from 0 to 63 integers,
#       printing out a message when the underlying capacity of the list changes. Recall that the
#       capacity of the list is the number of elements that can be stored (sys.getsizeof is
#       your friend here, but remember that it returns sizes expressed in bytes!).

def main():
    growthList = []
    sizeOfList = sys.getsizeof(growthList)
    print('size of list:', sizeOfList)

    for i in range(0, 64):
        growthList.append(i)
        if sys.getsizeof(growthList) > sizeOfList:
            sizeOfList = sys.getsizeof(growthList)
            print("size of list has increased:", sizeOfList)
    

if __name__ == '__main__':
    main()