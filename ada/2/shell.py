import time
from decimal import *

def Shell_Sort(list):
    size = len(list)
    gap = int(size / 2)

    while gap > 0:
        for i in range(gap, size):
            temp = list[i]

            j = i
            while  j >= gap and list[j - gap] > temp:
                list[j] = list[j - gap]
                j -= gap

            list[j] = temp
        gap = int(gap / 2)

def Print_list(list):
    for i in range(len(list)):
        print(list[i], end = " ")

    print()

print("Input a list of numbers separated by spaces")
list = [int(x) for x in input().split()]
start=time.time()
Shell_Sort(list)
end = time.time()

print("Sorted list:",list)
print("Execution time:",Decimal(end-start))
