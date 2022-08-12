import pandas as pd
import pingouin as pg

io = r'D:/Y4/ML/Results.xls'
f = pd.read_excel(io, sheet_name=2, usecols=[8,9,10])
f.head()
for i in range(len(f)):
    print(f.loc[i])

corr=pg.pairwise_corr(f, method='pearson')
spearman_corr=pg.pairwise_corr(f, method='spearman')
kendall_corr=pg.pairwise_corr(f, method='kendall')
bicor_corr=pg.pairwise_corr(f, method='bicor')
skipped_corr=pg.pairwise_corr(f, method='skipped')
corr=corr.append(spearman_corr)
corr=corr.append(kendall_corr)
corr=corr.append(bicor_corr)
corr=corr.append(skipped_corr)

corr.to_excel('D:/Y4/ML/correlation1.xls')



