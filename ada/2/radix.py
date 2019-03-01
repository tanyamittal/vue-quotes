import time
from decimal import *
def Counting_Sort(list, exp):
    size = len(list)
    output = [0] * size
    count = [0] * 10

    for i in range(0, size):
        count[int(list[i] / exp) % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(size - 1, -1, -1):
        output[count[int(list[i] / exp) % 10] - 1] = list[i]
        count[int(list[i] / exp) % 10] -= 1

    for i in range(0, size):
        list[i] = output[i]

def Radix_Sort(list):
    maximum = max(list)

    exp = 1
    while int(maximum / exp) > 0:
        Counting_Sort(list, exp)
        exp *= 10


print("Input a list of numbers separated by spaces")
list = [int(x) for x in input().split()]
start=time.time()
Radix_Sort(list)
end = time.time()

print("Sorted list:",list)
print("Execution time:",Decimal(end-start))
