import time
from decimal import *

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
    return alist

print("Input a list of numbers separated by spaces")
alist = [int(x) for x in input().split()]
start = time.time()
print("Sorted list",bubbleSort(alist))
end = time.time()
print("Execution time:",Decimal(end-start))
