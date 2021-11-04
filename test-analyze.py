import random
import matplotlib.pyplot as plt
import numpy as np
import math

def bubbleSort(arr):
    cnt = 0
    n = len(arr)

	# Traverse through all array elements
    for i in range(n-1):
	# range(n) also work but outer loop will repeat one time more than needed.

		# Last i elements are already in place
    	for j in range(0, n-i-1):

			# traverse the array from 0 to n-i-1
			# Swap if the element found is greater
			# than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                cnt += 1
    allcnt.append(cnt)
    

allcnt = []
arr = []

cntx = []
cntamnt = []




for x in range(200):
    arr.append(x)
    cntamnt.append(x)
    allcnt = []
    for _ in range(10):
        random.shuffle(arr)
        bubbleSort(arr)
    cntx.append(sum(allcnt)/len(allcnt))



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
plt.ylim(0, 1000)

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
'''