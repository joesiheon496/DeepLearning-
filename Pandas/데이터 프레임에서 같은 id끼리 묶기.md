'''python
import pandas as pd

# Sample data
data = {'id': [1, 1, 2, 2, 3],
        'value': [10, 20, 30, 40, 50]}

df = pd.DataFrame(data)

# 같은 id의 값들끼리 모으기
grouped = df.groupby(['id'])['value'].apply(list).reset_index(name='new_value')

print(grouped)
'''
