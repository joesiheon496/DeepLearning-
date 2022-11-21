```python
import pandas as pd
df = pd.read_csv('')

df_1 = np.load('')

df['after'] = 0
for i,v in enumerate(df.columns_name):
  df['after'].loc[i] = np.array(df_1[i],dtype=object)
```
