import os
forders = os.listdir('파일위치')

df_all_data = pd.DataFrame()

for files in forders[:-1]:
	df = pd.read_csv(f'파일위치/{files}',dtype = {'열의 데이터 형태 지정'}) #,parse_dates=['Date']
	df_all_data = pd.concat([df_all_data,df])
