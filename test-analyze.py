import random
from types import AsyncGeneratorType
import matplotlib.pyplot as plt
import numpy as np


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
x = np.array(cntx)
y = np.array(cntamnt)
plt.plot(y, x)
plt.show()



'''
print("highest count number: ")
print(max(allcnt))
print("gjennomsnitt av counters: ")
print(sum(allcnt) / len(allcnt))
'''