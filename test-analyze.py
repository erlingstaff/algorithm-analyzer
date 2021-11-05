import random
import matplotlib.pyplot as plt
import numpy as np
import math
import time
import timeit


cnt = 0
def mergeSort(myList):

    global cnt
    cnt += 1
    if len(myList) > 1:

        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]

        # Recursive call on each half
        mergeSort(left)
        mergeSort(right)

        # Two iterators for traversing the two halves
        i = 0
        j = 0
        
        # Iterator for the main list
        k = 0
        
        while i < len(left) and j < len(right):
            cnt +=1
            if left[i] <= right[j]:
              # The value from the left half has been used
              myList[k] = left[i]
              # Move the iterator forward
              i += 1
            else:
                myList[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(left):
            cnt+=1
            myList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            cnt +=1

            myList[k]=right[j]
            j += 1
            k += 1

def callfunc(arr):
    #random.shuffle(arr)
    #mergeSort(arr)
    finda(arr)



def bubbleSort(arr):
    cnt = 0
    n = len(arr)
    cnt += 1

    for i in range(n-1):
        for j in range(0, n-i-1):
            cnt +=1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                cnt += 1
    allcnt.append(cnt)
    

def selection_sort(A):
    cnt = 0
    for i in range(len(A)):
        
        min_idx = i

        for j in range(i+1, len(A)):
            if A[min_idx] > A[j]:
                min_idx = j
            cnt += 1
        A[i], A[min_idx] = A[min_idx], A[i]
    allcnt.append(cnt)


def finda(a):
    pass
    cnt = 0


    #allcnt.append(cnt)




allcnt = []
arr = []

cntx = []
cntamnt = []
global timerr
timerr = []

for x in range(200):
    arr.append(x)
    cntamnt.append(int(x))
    allcnt = []
    #timerr.append(timeit.timeit(lambda: callfunc(arr), number=100))
    #timerr.append(timeit.timeit(lambda: callfunc(arr), number=100)/100)
    for _ in range(10):
        random.shuffle(arr)
        cnt = 0
        mergeSort(arr)
        allcnt.append(cnt)
    cntx.append(max(allcnt))
    #print(max(timer))
    #print(timer)
'''
print("ABCD", timerr[0])
yy = [0.5 for _ in range(200)]
print("BBB", yy[0])

plt.figure(figsize=(14,8))
xb = np.array(timerr)
yb = np.array(yy)


plt.plot(xb)
plt.legend()
plt.show()

'''


def determine():
    dy = cntx
    dx = cntamnt


determine()
plt.figure(figsize=(14,8))
y = np.array(cntx)
x = np.array(cntamnt)
xfac = np.array([x for x in range(10)])
y2 = np.array([x*x for x in range(200)])
y3 = np.array([1 for _ in range(200)])
y4 = np.array([math.log(x+1, 10) for x in range(200)])
y5 = np.array([x for x in range(200)])
y6 = np.array([(x+1)*(math.log(x+1, 10)) for x in range(200)])
y7 = np.array([2**x for x in range(200)])
y8 = np.array([math.factorial(x) for x in range(10)])



plt.plot(x, y, label="Algorithm")
plt.plot(x, y2, label="O(n^2)")
plt.plot(x, y3, label="O(1)")
plt.plot(x, y4, label="O(log n)")
plt.plot(x, y5, label="O(n)")
plt.plot(x, y6, label="O(n log n)")
plt.plot(x, y7, label="O(2^n)")
plt.plot(xfac, y8, label="O(n!)")



plt.legend()
plt.ylim(0, 25000)
plt.show()

def generate_functions():
    pass


def evaluate():
    pass


'''
print("highest count number: ")
print(max(allcnt))
print("gjennomsnitt av counters: ")
print(sum(allcnt) / len(allcnt))


a = cntamnt[:50]
b = cntx[:50]

for x in range(len(a)-1):
    print((a[x] - b[x]) - (a[x+1] - b[x+1]))


'''

print()