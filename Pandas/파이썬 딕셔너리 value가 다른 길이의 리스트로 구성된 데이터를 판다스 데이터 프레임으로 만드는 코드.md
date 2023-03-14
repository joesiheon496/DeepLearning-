import pandas as pd

# Sample data
my_dict = {'A': [1, 2, 3], 'B': [4, 5], 'C': [6, 7, 8, 9]}

# 딕셔너리를 데이터프레임으로 변환하기
df = pd.DataFrame.from_dict(my_dict, orient='index').T

print(df)
