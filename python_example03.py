import pandas as pd

data = {"이름": ["철수", "영희", "민수"], "나이": [25, 30, 35]}
df = pd.DataFrame(data)

print(df.describe())