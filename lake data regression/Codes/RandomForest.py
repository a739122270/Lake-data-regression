import math

import xlrd
import xlwt
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor, ExtraTreesRegressor
import random
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import SimpleImputer, IterativeImputer
from pandas import Series, DataFrame
from numpy import nan as NaN
from sklearn.linear_model import BayesianRidge
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsRegressor
from sklearn.pipeline import make_pipeline
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeRegressor

N_SPLITS = 5
io = r'D:/Y4/ML/Results.xls'
data = pd.read_excel(io, sheet_name=0, usecols=[5, 6, 8])
data.head()
X = data[['Year', 'Month']]
y = data['CHLA （mg/L）']

sample = data.copy()
sample.dropna(axis=0, how='any', inplace=True)
sample.reset_index(drop=True, inplace=True)
X = sample.copy()
X_full=sample[['Year','Month']]
y_full=sample['CHLA （mg/L）']
X_missing=X[['Year','Month']]
y_missing=X['CHLA （mg/L）']


# Accuracy
missing_rate=0.2
missing_number= math.floor(0.2 * 77)

X_missing=np.array(X_missing)
X_missing = X_missing.astype(np.float)
# print(X_missing)
missing_index=[]
# y_true=[]
i=0
while i< missing_number:
     tem= random.randint(0,76)
     tem2 = random.randint(0, 1)
     if (tem,tem2) not in missing_index:
         missing_index.append([tem,tem2])
         # y_true.append(round(missing[tem,2],7))
         X_missing[tem,tem2]=np.nan
         i=i+1
     else:
         i=i-1
print(X_missing)
# imp = IterativeImputer(missing_values=np.nan, estimator= RandomForestRegressor(random_state=0), random_state=0)
# imp.fit(missing)
# impute_missing = imp.transform(missing)
# print(impute_missing)
# print(impute_missing[:,2])

# y_predict=[]
# for i in range(len(missing_index)):
#     y_predict.append(round(impute_missing[missing_index[i],2],7))
# print(y_true)
# print(y_predict)
#
# print(accuracy_score(y_true, y_predict))




#mse
# br_estimator = BayesianRidge()
# score_full_data = pd.DataFrame(
#     cross_val_score(
#         br_estimator, X_full, y_full, scoring='neg_mean_squared_error',
#         cv=N_SPLITS
#     ),
#     columns=['Full Data']
# )
# # Estimate the score after imputation (mean and median strategies)
# score_simple_imputer = pd.DataFrame()
# for strategy in ('mean', 'median'):
#     estimator = make_pipeline(
#         SimpleImputer(missing_values=np.nan, strategy=strategy),
#         br_estimator
#     )
#     score_simple_imputer[strategy] = cross_val_score(
#         estimator, X_missing, y_missing, scoring='neg_mean_squared_error',
#         cv=N_SPLITS
#     )
#
# # Estimate the score after iterative imputation of the missing values
# # with different estimators
# estimators = [
#     DecisionTreeRegressor(max_features='sqrt', random_state=0),
#     RandomForestRegressor(random_state=0, max_depth=10, n_estimators=100),
#     KNeighborsRegressor(n_neighbors=15)
# ]
# score_iterative_imputer = pd.DataFrame()
# for impute_estimator in estimators:
#     estimator = make_pipeline(
#         IterativeImputer(random_state=0, estimator=impute_estimator),
#         br_estimator
#     )
#     score_iterative_imputer[impute_estimator.__class__.__name__] = \
#         cross_val_score(
#             estimator, X_missing, y_missing, scoring='neg_mean_squared_error',
#             cv=N_SPLITS
#         )
#
# scores = pd.concat(
#     [score_full_data, score_simple_imputer, score_iterative_imputer],
#     keys=['Original', 'SimpleImputer', 'IterativeImputer'], axis=1
# )
# plot
# fig, ax = plt.subplots(figsize=(13, 6))
# means = -scores.mean()
# errors = scores.std()
# means.plot.barh(xerr=errors, ax=ax)
# ax.set_title('China Lake')
# ax.set_xlabel('MSE (smaller is better)')
# ax.set_yticks(np.arange(means.shape[0]))
# ax.set_yticklabels([" w/ ".join(label) for label in means.index.tolist()])
# plt.tight_layout(pad=1)
# plt.show()
imp = IterativeImputer(missing_values=np.nan,
                       estimator=RandomForestRegressor(random_state=0,max_depth=10, n_estimators=100),
                       random_state=0)
imp.fit(data)
data2 = imp.transform(data)

f = xlwt.Workbook()
sheetw2 = f.add_sheet('2', cell_overwrite_ok=True)

for i in range(len(data2)):
    d = data2[i]
    sheetw2.write(i + 1, 0, d[2])  # 第1行第1列
f.save('D:/Y4/ML/SAVE.xls')
