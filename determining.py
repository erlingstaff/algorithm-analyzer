from random import randint

def isO1(y, x):
    start = randint(0, len(y)-20)
    nums = []
    for i in range(start):
        nums.append(y[i])
    if nums.count(nums[0]) == len(nums):
        print("O(1)")
    

def isOn(y, x):
    start = randint(0, len(y)-20)
    nums = []
    numsdiff = []
    for i in range(start):
        nums.append(y[i])
        if i != 0:
            numsdiff.append(y[i]-y[i-1])        
    if numsdiff.count(numsdiff[0]) == len(numsdiff):
        print("O(n)")

    

