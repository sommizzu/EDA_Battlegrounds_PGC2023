#library
import os
import glob
import math
import swifter
import pandas as pd
from datetime import datetime

#파일 함수
from landing_1st import landing_processing

# 전체데이터 전처리
tel_eragnel = ['tel4','tel5','tel6','tel7','tel16','tel17']
tel_mirama = ['tel0', 'tel1','tel10','tel11', 'tel12', 'tel13']
tel_vikendi = ['tel3','tel8','tel15']
tel_taego = ['tel2','tel9','tel14']

tel_map = [tel_eragnel,tel_mirama,tel_vikendi,tel_taego]

tel_list = ['tel0','tel1','tel2','tel3','tel4','tel5','tel6','tel7','tel8','tel9','tel10',\
            'tel11', 'tel12', 'tel13', 'tel14', 'tel15', 'tel16', 'tel17']

for i in tel_list:
    landing_processing(i)

combined_df_1 = pd.DataFrame()
combined_df_2 = pd.DataFrame()

# 합칠 CSV 파일들이 있는 디렉토리 경로
folder_path = r'C:\Users\PC\Desktop\AI_Lab\pubg\preprocessed'

# 합칠 특정 이름의 CSV 파일 목록
csv_files_1 = glob.glob(f"{folder_path}/first_landing*.csv")
csv_files_2 = glob.glob(f"{folder_path}/first_vehicle*.csv")

# 모든 CSV 파일을 순회하면서 데이터프레임에 추가
for file in csv_files_1:
    df = pd.read_csv(file)
    combined_df_1 = pd.concat([combined_df_1, df], ignore_index=True)

for file in csv_files_2:
    df = pd.read_csv(file)
    combined_df_2 = pd.concat([combined_df_2, df], ignore_index=True)

file_path_2 = f'C:/Users/PC/Desktop/AI_Lab/pubg/preprocessed/all_landing_location.csv'
file_path_3 = f'C:/Users/PC/Desktop/AI_Lab/pubg/preprocessed/all_vehicle_location.csv'

combined_df_1.to_csv(file_path_2, index=False)
combined_df_2.to_csv(file_path_3, index=False)

# 삭제할 CSV 파일들이 있는 디렉토리 경로
folder_path = r'C:\Users\PC\Desktop\AI_Lab\pubg\preprocessed'

# 삭제할 특정 이름의 CSV 파일 목록
files_to_delete = glob.glob(f"{folder_path}/first*.csv")

# 파일 삭제
for file in files_to_delete:
    os.remove(file)
