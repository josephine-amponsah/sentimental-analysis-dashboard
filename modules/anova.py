import pandas as pd
import seaborn as sns
#boxplot to observe distribution
def distPlot(data, var, col):
    sns.boxplot(data, x = var, y = col)
    
#observed mean
def observeddiff (col, val, data):
    data = data[[col, val]]
    newData = data.groupby(col).mean(val)
    a = newData[val].iloc[0]
    b = newData[val].iloc[1]
    return a-b if a>b else b-a

# permutation function 
import random
def permfunc (df, col, val):
    df = df[[col, val]]
    categories = df[col].value_counts()
    nA = categories.iloc[0]
    nB = categories.iloc[1]
    n = nA + nB
    idxA = set(random.sample(range(n), nA))
    idxB = set(range(n)) - idxA
    meanB = df.loc[idxB].mean()
    meanA = df.loc[idxA].mean()
    permmeandiff = abs(meanA - meanB)
    return permmeandiff