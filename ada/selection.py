import time
from decimal import *
print("Input a list of numbers separated by spaces")
a = [int(x) for x in input().split()]
def selectionSort(a):
    for i in range(len(a)):
        min = i
        for j in range(i+1,len(a)):
            if a[min]>a[j]:
                a[min],a[j] = a[j],a[min]
    return a

start = time.time()
print("Sorted list",selectionSort(a))
end = time.time()
print("Execution time:",Decimal(end-start))
