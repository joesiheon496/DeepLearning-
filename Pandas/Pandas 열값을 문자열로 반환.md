apply()메서드를 사용하여 DataFrame의 열 값 데이터 유형을 문자열로 변환
```python
employees_df["Age"]=employees_df["Age"].apply(str)
```
applymap()메서드를 사용하여 모든 DataFrame 열의 데이터 유형을string으로 변환
```python
employees_df=employees_df.applymap(str)
```
astype()메서드를 사용하여 DataFrame 열 값의 데이터 유형을string으로 변환
```python
employees_df["Score"]=employees_df["Score"].astype(str)
```
