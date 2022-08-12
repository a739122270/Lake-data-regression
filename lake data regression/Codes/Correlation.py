import pandas as pd
import numpy as np
import pingouin as pg


io = r'D:/Y4/ML/Results.xls'

data = pd.read_excel(io, sheet_name=2, usecols=[8,9,10])
data.head()
print(len(data))
for i in range(len(data)):
    print(data.loc[i])

a=pg.pairwise_corr(data, method='pearson')
b=pg.pairwise_corr(data, method='spearman')
c=pg.pairwise_corr(data, method='kendall')
d=pg.pairwise_corr(data, method='percbend')
e=pg.pairwise_corr(data, method='shepherd')
a=a.append(b)
a=a.append(c)
a=a.append(d)
a=a.append(e)

a.to_excel('D:/Y4/ML/correlation.xls')



