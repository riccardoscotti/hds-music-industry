import pandas as pd
import matplotlib.pyplot as plt
import ruptures as rpt

data = pd.read_csv("apkQuarter.csv")

dx = []
#dl=data['Downloads'].values
dl=data['Sum'].values

for i in data.index:
    dx.append(str(data['Year'][i]) + ' ' + str(data['Quarter'][i]))




n_bkps=3
algo = rpt.Dynp(model='rbf')
algo.fit(dl)
result = algo.predict(n_bkps=n_bkps)

'''

algo = rpt.Pelt(model="l2")
algo.fit(dl)
result = algo.predict(pen=1)

'''



rpt.display(dl, [], result)

plt.plot(dx, dl, label='Sum Downloads')
plt.xticks(rotation=90)
plt.legend() 
plt.show()