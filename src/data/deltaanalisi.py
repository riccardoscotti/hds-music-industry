import pandas as pd
from statsmodels.tsa.stattools import grangercausalitytests
import matplotlib.pyplot as plt
import ruptures as rpt

d=pd.read_csv('spoty.csv')
d = d.iloc[1:]

gp=d['Gross Profit'].values
year=d['Year'].values
quarter=d['Quarter'].values
dx=[]
for i in d.index:
    dx.append(str(d['Year'][i]) + ' ' + str(d['Quarter'][i]))

d=pd.read_csv('delta.csv')
delta=d['Delta'].values

df={'Gross Profit': gp, 'Delta': delta}
data=pd.DataFrame(data=df)

gc_res = grangercausalitytests(data[["Gross Profit", "Delta"]], maxlag=1)
print(gc_res)

gc_res = grangercausalitytests(data[["Delta", "Gross Profit"]], maxlag=1)
print(gc_res)

print(data.corr(method='pearson'))

'''
n_bkps=4
algo = rpt.Dynp(model='l1')
algo.fit(delta)
result = algo.predict(n_bkps=n_bkps)
'''

algo = rpt.Pelt(model="l2")
algo.fit(delta)
result = algo.predict(pen=1)


rpt.display(delta, [], result)
plt.plot(dx, delta, label='Delta')
plt.xticks(rotation=90)
plt.legend() 
plt.show()

