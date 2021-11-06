from random import randint
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import lmfit
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import FunctionTransformer
from sklearn.metrics import mean_absolute_error

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


    
    

# n-regression Functions

def lognfunc(x,a,b):
    return a * np.log(x) + b

def nlognfunc(x, a, b):
    return x * a * np.log(x) + b

def n2func(x, a, b):
    return a * (x * x) + b

def O2nfunc(x, a, b):
    return a * (2**x) * b


# O() check-functions

def isOlogn(y, x):

    plt.plot(x, y)
    
    x = np.array(x, dtype=float) 
    y = np.array(y, dtype=float)
    x[0] = x[1]
    y[0] = y[1]

    popt, _ = curve_fit(lognfunc, x, y, maxfev=100000)
    ploty = lognfunc(x, *popt)

    MAE = mean_absolute_error(y, ploty)
    print("Logarithmic regression O(log n) MAE:", MAE)

    plt.plot(x, ploty)
    plt.show()


def isOnlogn(y, x):

    plt.plot(x, y)
    
    x = np.array(x, dtype=float)
    y = np.array(y, dtype=float)
    x[0] = x[1]
    y[0] = y[1]

    popt2, _ = curve_fit(nlognfunc, x, y, maxfev=100000)

    ploty2 = nlognfunc(x, *popt2)

    MAE2 = mean_absolute_error(y, ploty2)
    print("n * Logarithmic regression O(n log n) MAE:", MAE2)

    plt.plot(x, ploty2)
    plt.show()


def isOn2(y, x):

    plt.plot(x, y)
    
    x = np.array(x, dtype=float)
    y = np.array(y, dtype=float)
    x[0] = x[1]
    y[0] = y[1]

    popt, _ = curve_fit(n2func, x, y, maxfev=100000)

    ploty = n2func(x, *popt)

    MAE = mean_absolute_error(y, ploty)
    print("Quadratic regression O(n^2) MAE:", MAE)

    plt.plot(x, ploty)
    plt.show()


def isO2n(y, x):

    plt.plot(x, y)
    
    x = np.array(x, dtype=float)
    y = np.array(y, dtype=float)
    x[0] = x[1]
    y[0] = y[1]

    popt, _ = curve_fit(O2nfunc, x, y, maxfev=100000)

    ploty = O2nfunc(x, *popt)

    MAE = mean_absolute_error(y, ploty)
    print("Exponential regression O(2^n) MAE:", MAE)

    plt.plot(x, ploty)
    plt.show()
