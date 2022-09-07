## 문제
dictionary로 지정 후 value 값들을 리스트로 뽑고싶었었다.
그래서 방법을 찾은 결과
```python
dictionary = {}
dictionary['value들'] = 0
print(list(dictionary.values()))
```
를 해주면 value들이 list로 나오게된다.
만약 key값을 list로 뽑고 싶다면
```python
print(list(dictionary.keys()))
```
로 하면 된다.
