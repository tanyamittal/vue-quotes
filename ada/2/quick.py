import time
from decimal import *

# Conquer
def Parition(list, left, right):
    pivot = list[left]
    index = right

    for j in range(right, left - 1, -1):
        if list[j] > pivot:
            list[index], list[j] = list[j], list[index]
            index -= 1

    list[index], list[left] = list[left], list[index]
    return index

# Divide list into halves
def Quick(list, left, right):
    if left < right:
        pivot = Parition(list, left, right)

        Quick(list, left, pivot - 1)
        Quick(list, pivot + 1, right)

def Quick_Sort(list):
    Quick(list, 0, len(list) - 1)

print("Input a list of numbers separated by spaces")
list = [int(x) for x in input().split()]
start=time.time()
Quick_Sort(list)
end = time.time()

print("Sorted list:",list)
print("Execution time:",Decimal(end-start))
