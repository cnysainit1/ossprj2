import pandas as pd
data_df = pd.read_csv('2019_kbo_for_kaggle_v2.csv')

# 1
print("1:")
arr = ['H', 'avg', 'HR', 'OBP']
for x in arr:
    for year in range(2015, 2019):
        print(x, year)
        print(data_df[data_df['year'] == year].sort_values(by=x, ascending=False)['batter_name'][:10])
    print()

# 2
position_info = ['포수', '1루수', '2루수', '3루수', '유격수', '좌익수', '중견수', '우익수']
temp_df = data_df[data_df['year'] == 2018].sort_values(by='war', ascending=False)
print("2:")
for x in position_info:
  print(x + ' ' + temp_df[temp_df['cp'] == x].iloc[0]['batter_name'])

# 3
corr_df = data_df[['R', 'H', 'HR', 'RBI', 'SB', 'war', 'avg', 'OBP', 'SLG']].corrwith(data_df['salary']).sort_values(ascending=False)
print("\n3:")
print(corr_df)
print("the highest correlation with salary is", corr_df.index[0])