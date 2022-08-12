import pandas as pandas
import matplotlib.pyplot as plt 
import numpy as np
import seaborn as sns 
import random
'''
    Module for performing chi square analysis for A/B/C testing
'''

#def expectedVal (data, col1, col2):
    #return  sum(data[col1])/ sum(data[col2])

#def rValue ():
def chi2(observed, expected):
    pearson_residuals = [[(observe - expect) ** 2 / expect
    for observe in row] for row, expect in zip(observed, expected)] 
    # return sum of squares
    return np.sum(pearson_residuals)

def perm_fun(box, expected, total):
    sample_clicks = [sum(random.sample(box, total)),
    sum(random.sample(box, total)),
    sum(random.sample(box, total))]
    return chi2([sample_clicks], expected)

def perm_chi(box, ranges):
    for _ in range(ranges):
        perm_chi2 = [perm_fun(box)]
    return perm_chi2

#def perm_plot(permdata):