from sklearn.preprocessing import LabelEncoder
input_labels = ['삼성전자','애플','테슬라','페이스북','넷플릭스']
encoder = LabelEncoder()
# 레이블 학습
encoder.fit(input_labels)

# print labels

for i, label in enumerate(encoder.classes_):
  print(i, '->', label)
  
'''
0 -> 넷플릭스
1 -> 삼성전자
2 -> 애플
3 -> 테슬라
4 -> 페이스북
'''
test_labels = ['넷플릭스','테슬라']
encoder.transform(test_labels)
# ['넷플릭스','테슬라'] -> [0,3]

# 디코딩
encode_datas = [2,4,1]
encoder.inverse_transform(encode_datas)
