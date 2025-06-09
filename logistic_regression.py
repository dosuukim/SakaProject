
# python logistic_regression.py

import pandas as pd
# import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

file_url = 'https://media.githubusercontent.com/media/musthave-ML10/data_source/main/titanic.csv'

data = pd.read_csv(file_url)
################# df = pd.DataFrame(data)

# print(data) # 데이터셋 출력
# print(data.head(5)) # 상위5개 출력
# print(data.info()) # 변수특징 출력
# print(round(data.describe(), 2)) # 통계정보 출력
# print(data.corr(min_periods=1)) # 상관관계 출력
# print(data.corr()) # 상관관계 출력
################ -------------print(df.corr())

sns.heatmap(data.corr())
plt.show()
