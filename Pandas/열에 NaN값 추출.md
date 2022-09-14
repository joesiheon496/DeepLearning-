해당 열에 NaN값을 추출하는 코드
```python
df[df['A'].isnull()]
```
해당 열이 Nan이라면 빼는코드 실험중
```python
df[df['A'].isnull() == False]
```
전에했던
```python
sample_train = sample_train[sample_train.A_abstract.str.contains("")==False]
```
로도 해결가능
