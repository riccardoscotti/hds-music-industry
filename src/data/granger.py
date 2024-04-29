import pandas as pd
from statsmodels.tsa.stattools import grangercausalitytests

data = pd.read_csv("spoty.csv")

'''
gc_res = grangercausalitytests(data[["Gross Profit", "Ad Gross Profit"]], maxlag=1)

print(gc_res)
'''

'''
gc_res = grangercausalitytests(data[["Gross Profit", "Premium MAUs"]], maxlag=1)

print(gc_res)
'''

'''
gc_res = grangercausalitytests(data[["Gross Profit", "Ad MAUs"]], maxlag=1)

print(gc_res)
'''

'''
gc_res = grangercausalitytests(data[["Gross Profit", "Research and Development Cost"]], maxlag=1)

print(gc_res)
'''


data = pd.read_csv("all.csv")


'''
gc_res = grangercausalitytests(data[["Gross Profit", "Apk Downloads"]], maxlag=1)

print(gc_res)
'''

gc_res = grangercausalitytests(data[["Premium MAUs", "Apk Downloads"]], maxlag=1)

print(gc_res)

gc_res = grangercausalitytests(data[["Apk Downloads","Premium MAUs"]], maxlag=1)

print(gc_res)
