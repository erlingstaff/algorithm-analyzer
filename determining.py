from random import randint
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from sklearn.metrics import mean_absolute_error
from scipy.special import factorial




# O(1) and O(n) checker functions

def isO1(y, _):
    try:
        start = len(y)
        nums = []
        for i in range(start):
            nums.append(y[i])
        if nums.count(nums[0]) == len(nums):
            return True
        else:
            return False
    except:
        return True
    

def isOn(y, _):
    try:
        start = len(y)
        nums = []
        numsdiff = []
        for i in range(start):
            nums.append(y[i])
            if i != 0:
                numsdiff.append(y[i]-y[i-1])
        if numsdiff.count(numsdiff[0]) == len(numsdiff):
            return True
        else:
            return False
    except:
        return False


# O(n)-regression Functions

def lognfunc(x,a,b):
    return a * np.log(x) + b

def nlognfunc(x, a, b):
    return x * a * np.log(x) + b

def n2func(x, a, b):
    return a * (x * x) + b

def O2nfunc(x, a, b):
    return a * (2**x) + b

def nfacfunc(x, a, b):
    x = factorial(x)
    return a * x + b



# O() check-functions

def isOlogn(y, x):

    try:
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
        return (MAE, "O(log n)")
    except:
        return (-1, MAE("O(log n)"))


def isOnlogn(y, x):

    try:
        plt.plot(x, y)
        
        x = np.array(x, dtype=float)
        y = np.array(y, dtype=float)
        x[0] = x[1]
        y[0] = y[1]

        popt, _ = curve_fit(nlognfunc, x, y, maxfev=100000)

        ploty = nlognfunc(x, *popt)

        MAE = mean_absolute_error(y, ploty)
        print("n * Logarithmic regression O(nlog n) MAE:", MAE)

        plt.plot(x, ploty)
        plt.show()
        return (MAE, "O(nlog n)")

    except:
        return (-1, "O(nlog n)")


def isOn2(y, x):
    try:
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
        return (MAE, "O(n^2)")

    except:
        return (-1, "O(n^2")


def isO2n(y, x):

    try:
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
        return (MAE, "O(2^n)")

    except:
        return (-1, "O(2^n)")


def isOfacn(y, x):
    try:
            
        plt.plot(x, y)
        
        x = np.array(x, dtype=float)
        y = np.array(y, dtype=float)
        x[0] = x[1]
        y[0] = y[1]

        popt, _ = curve_fit(nfacfunc, x, y, maxfev=100000)

        ploty = nfacfunc(x, *popt)

        MAE = mean_absolute_error(y, ploty)
        print("Factorial regression O(!n) MAE:", MAE)

        plt.plot(x, ploty)
        plt.show()
        return (MAE, "O(!n)")

    except:
        return (-1, "O(!n)")


