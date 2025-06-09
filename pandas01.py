#  python pandas01.py

# import pandas as pd
# file_url = 'https://media.githubusercontent.com/media/musthave-ML10/data_source/main/insurance.csv'

# data = pd.read_csv(file_url)

# print(data.head(5))
# print(data.info())
# print(round(data.describe(), 2))


# -------------------------------------------------------------------
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split # 사이킷런 임포트
from sklearn.linear_model import LinearRegression


file_url = 'https://media.githubusercontent.com/media/musthave-ML10/data_source/main/insurance.csv'

data = pd.read_csv(file_url)

X = data[['age', 'sex', 'bmi', 'children', 'smoker']] # 독립변수
y = data['charges'] # 종속변수

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=100) # 데이터셋 분할

model = LinearRegression()
model.fit(X_train, y_train)

pred = model.predict(X_test)
# print(pred)

comparison = pd.DataFrame({'actual' : y_test, 'pred' : pred})
# print(comparison)

plt.figure(figsize=(10, 10))
sns.scatterplot(x = 'actual', y = 'pred', data = comparison)
plt.show() # 산점도 그래프 보기

# # # print(sns)

# from sklearn.metrics import mean_squared_error
# # mean_squared_error(y_test, pred) ** 0.5
# # print(mean_squared_error(y_test, pred) ** 0.5)
# # mean_squared_error(y_test, pred, squared = False)
# print(model.score(X_train, y_test))
