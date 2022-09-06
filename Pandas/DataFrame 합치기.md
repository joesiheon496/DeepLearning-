# DataFrame 합치기는 다음과 같다.

```python
pd.concat(['df1','df2'],axis = 0,ignore_index=True) # axis = 0 은 아래로 붙이기 1은 오른쪽으로 붙이기다
```
기존의 index를 무시해 주는 경우가 편했다.

계층 인덱스를 만들어 주려면 다음과 같다

```python
pd.concat(['df1','df2'],axis = 0,ignore_index=True)
```
