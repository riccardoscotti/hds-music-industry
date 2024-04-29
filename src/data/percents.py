import pandas as pd
import matplotlib.pyplot as plt
import ruptures as rpt

data = pd.read_csv("spoty.csv")

dx = []
gp=data['Gross Profit'].values
pgp=data['Premium Gross Profit'].values
agp=data['Ad Gross Profit'].values
mau=data['MAUs'].values
pmau=data['Premium MAUs'].values
amau=mau=data['Ad MAUs'].values

pGpMau=[]
pGpPMau=[]
pPMauMau=[]

for i in data.index:
    dx.append(str(data['Year'][i]) + ' ' + str(data['Quarter'][i]))
    pGpMau.append(data['Gross Profit'][i] / data['MAUs'][i])
    pGpPMau.append(data['Gross Profit'][i] / data['Premium MAUs'][i])
    pPMauMau.append(data['MAUs'][i] / data['Premium MAUs'][i])

plt.plot(dx, pGpMau, label='GP per User')
plt.plot(dx, pGpPMau, label='GP per Premium')
plt.plot(dx, pPMauMau, label='Users/Premium')
plt.xticks(rotation=90)
plt.legend() 
plt.show()

