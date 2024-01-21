#library
import os
import glob
import math
import swifter
import pandas as pd
from datetime import datetime

#파일 함수
from character_1st import character_processing

# 전체데이터 전처리
tel_eragnel = ['tel4','tel5','tel6','tel7','tel8','tel17']
tel_mirama = ['tel0', 'tel1','tel10','tel11', 'tel12', 'tel13']
tel_vikendi = ['tel3','tel16','tel15']
tel_taego = ['tel2','tel9','tel14']

tel_map = [tel_eragnel,tel_mirama,tel_vikendi,tel_taego]

tel_map_name = ['tel_eragnel','tel_mirama','tel_vikendi','tel_taego']

for i in range(0,len(tel_map)):

    combined_df_1 = pd.DataFrame()

    for i2 in tel_map[i]:
        character_processing(i2)     

    # 합칠 CSV 파일들이 있는 디렉토리 경로
    folder_path = r'C:\Users\PC\Desktop\AI_Lab\pubg\preprocessed'

    # 합칠 특정 이름의 CSV 파일 목록
    csv_files_1 = glob.glob(f"{folder_path}/character_location_*.csv")

    # 모든 CSV 파일을 순회하면서 데이터프레임에 추가
    for file in csv_files_1:
        df = pd.read_csv(file)
        combined_df_1 = pd.concat([combined_df_1, df], ignore_index=True)

    file_path_2 = f'C:/Users/PC/Desktop/AI_Lab/pubg/preprocessed/all_charcter_location_{i2}.csv'

    combined_df_1.to_csv(file_path_2, index=False)

    # 삭제할 CSV 파일들이 있는 디렉토리 경로
    folder_path = r'C:\Users\PC\Desktop\AI_Lab\pubg\preprocessed'

    # 삭제할 특정 이름의 CSV 파일 목록
    files_to_delete = glob.glob(f"{folder_path}/character_location*.csv")

    # 파일 삭제
    for file in files_to_delete:
        os.remove(file)