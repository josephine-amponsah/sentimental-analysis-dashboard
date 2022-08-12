import random
import pandas as pd
import numpy as np
import scipy
import matplotlib.pyplot as plt
import seaborn as sns
# boxplot to observe distribution


def distPlot(data, var, col):
    sns.boxplot(data, x=var, y=col)
    plt.plot()

# observed mean


def observeddiff(col, val, data):
    data = data[[col, val]]
    newData = data.groupby(col).mean(val)
    a = newData[val].iloc[0]
    b = newData[val].iloc[1]
    return a-b if a > b else b-a


# permutation function


def permfunc(df, col, val):
    df = df[[col, val]]
    categories = df[col].value_counts()
    nA = categories.iloc[0]
    nB = categories.iloc[1]
    n = nA + nB
    idxA = set(random.sample(range(n), nA))
    idxB = set(range(n)) - idxA
    meanB = df.loc[idxB].mean()
    meanA = df.loc[idxA].mean()
    return  abs(meanA - meanB)

#simulating permutation of
def permdiff(data, cat, var, range):
    permdiffs = []
    for _ in range:
        permfunc(data, cat, var)
        permdiffs.append()
    return permdiffs

#plotting permutations against observed mean values
def permPlot(diffs, catdiff):
    diffs = pd.DataFrame(diffs)
    sns.histplot(data = diffs,  bins = 10)
    plt.vlines(x= catdiff, ymin = 0, ymax =250, colors='blue')
    plt.plot()