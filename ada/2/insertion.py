import time
from decimal import *
def insertionSort(alist):
    for i in range (1,len(alist)):
        key = alist[i]
        j=i-1
        while j>=0 and key <alist[j]:
            alist[j+1]=alist[j]
            j=j-1
        alist[j+1]=key
    return alist
alist=[]
print("Insertion sort:-")
size = int(input("Enter size of the list:\t"))
for n in range(size):
    num = int(input("Enter the number"))
    alist.append(num)
print("\n The list is :",alist)
start = time.time()
sortedlist = insertionSort(alist)
end = time.time()
print("The sorted list is:",sortedlist)
print("exec_time",Decimal(end-start))
