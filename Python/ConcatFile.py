import os
forders = os.listdir('D:/patent_dataset/0928crawlingdata')

df_all_data = pd.DataFrame()

for files in forders[:-1]:
	df = pd.read_csv(f'위치',dtype = {'열의 데이터 형태 지정'}) #,parse_dates=['Date']
	df_all_data = pd.concat([df_all_data,df])
