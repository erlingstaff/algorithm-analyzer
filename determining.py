from random import randint
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import lmfit
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import FunctionTransformer


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


    
    

# General Functions
def func(x, a, b, c):
   return a * x * np.log(x*b) + c


def isOlogn(y, x):

    # LOGARITHMIC REGRESSION, CHECK MAE AND COMPARE TO OTHER REGRESSIONS
    
    x = np.array(x)
    y = np.array(y)
    popt, pcov = curve_fit(func, x, y, maxfev=100000)


    plt.plot(x, y, ls="none", marker='.')
    plt.plot(x, func(x, *popt),'-')
    plt.show()
