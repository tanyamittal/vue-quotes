import time
from decimal import *
# Conquer
def conquer_merge(alist, left, right, mid):
    #temp = [None] * len(alist)
    i = left
    j = mid + 1
    k = left

    while i <= mid and j <= right:
        if alist[i] <= alist[j]:
            temp[k] = alist[i]
            i += 1
        else:
            temp[k] = alist[j]
            j += 1
        k += 1

    while i <= mid:
        temp[k] = alist[i]
        i += 1
        k += 1

    while j <= right:
        temp[k] = alist[j]
        j += 1
        k += 1

    while left <= right:
        alist[left] = temp[left]
        left += 1

# Divide alist into halves
def divide(alist, left, right):
    if left < right:
        mid = left + (right - left) / 2;
        mid = int(mid)

        divide(alist, left, mid)
        divide(alist, mid + 1, right)

        conquer_merge(alist, left, right, mid)

def Merge_Sort(alist):
    global temp
    temp = [0] * len(alist)
    divide(alist, 0, len(alist) - 1)
    del temp

print("Input a list of numbers separated by spaces")
alist = [int(x) for x in input().split()]
start = time.time()
Merge_Sort(alist)
en = time.time()
print("Sorted list:",alist)
print("Execution time:",Decimal(en-start))
