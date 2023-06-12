import pandas as pd

# csv 파일 읽기
df = pd.read_csv('def_reservation.csv')

# "dogName"과 "dogSize"를 기준으로 중복 행 찾기
duplicated_dogs = df.duplicated(subset=['dogName', 'dogSize'], keep=False)

# 중복된 행만 선택
duplicated_df = df[duplicated_dogs]

# "dogName"으로 그룹화하고, 각 그룹의 크기 계산
counts = duplicated_df.groupby('dogName').size()

# 중복 횟수가 많은 순으로 정렬하고 상위 5개 선택
top_5 = counts.sort_values(ascending=False).head(5)

# 결과를 txt 파일에 쓰기
with open('top_5_duplicated_dog_names.txt', 'w') as f:
    for name, count in top_5.items():
        f.write(f'{name}: {count}\n')
