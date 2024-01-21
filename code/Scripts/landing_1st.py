#library
import math
import swifter
import pandas as pd
from datetime import datetime

def landing_processing(file_name):
    
    file_path = f'C:/Users/PC/Desktop/AI_Lab/pubg/data/{file_name}.csv'

    #파일 불러오기
    df = pd.read_csv(file_path)

    #필요한 컬럼별로 dataframe 구성
    df1=df[['_D','character.name', 'character.location.x', 'character.location.y','item.itemId']]
    df2=df[['_D','character.name', 'character.location.x', 'character.location.y','vehicle.vehicleType']]

    #저장진행
    df1.to_csv(r'C:\Users\PC\Desktop\AI_Lab\pubg\tel_processing\landing.csv', index=False)
    df2.to_csv(r'C:\Users\PC\Desktop\AI_Lab\pubg\tel_processing\vehicle.csv', index=False)

    df1 = pd.read_csv(r'C:\Users\PC\Desktop\AI_Lab\pubg\tel_processing\landing.csv')
    df2 = pd.read_csv(r'C:\Users\PC\Desktop\AI_Lab\pubg\tel_processing\vehicle.csv')
    df3 = pd.read_csv(r'C:\Users\PC\Desktop\AI_Lab\pubg\tel_processing\gameState.csv')

    #전처리
    df1 = df1.dropna()
    df2 = df2.dropna()
    df3 = df3.dropna()

    df1['_D'] = pd.to_datetime(df1['_D']).dt.strftime('%H:%M:%S.%f').str[:-3]
    df2['_D'] = pd.to_datetime(df2['_D']).dt.strftime('%H:%M:%S.%f').str[:-3]
    df3['_D'] = pd.to_datetime(df3['_D']).dt.strftime('%H:%M:%S.%f').str[:-3]

    #선수별 낙하 위치 및 시간계산
    df1 = df1[df1['item.itemId'] == 'Item_Back_B_01_StartParachutePack_C']
    df1 = df1.drop_duplicates(subset='character.name', keep='last')

    # TransportAircraft 는 수송기로 값 제외
    df2 = df2[df2['vehicle.vehicleType'] != 'TransportAircraft']

    # 어떤 vehicle이던 최초 사용기록만 남기면 첫 차량탑승 시간 및 위치표시가능 
    df2 = df2.drop_duplicates(subset='character.name', keep='first')

    df3_sample = df3[['_D','common.isGame','gameState.safetyZoneRadius']]

    df3_start = df3_sample.drop_duplicates('common.isGame', keep='first')
    df3_end = df3_sample.drop_duplicates('common.isGame', keep='last')

    # df2_start, end 값 비교하여 볼수 있도록 df2_phase 구성
    df3_phase = pd.merge(df3_start, df3_end, on='common.isGame')
    df3_phase = df3_phase[['common.isGame','_D_x','_D_y']]

    # 시간이 얼추 10초단위로 기록됨
    df3_phase.columns = ['phase','start_time','end_time']

    def time_to_float(row):
        time_data = row['_D']
        hours, minutes, seconds = map(float, time_data.split(':'))
        time_data = hours * 3600 + minutes * 60 + seconds

        return  time_data

    # 선수별 시간 데이터 : 수치상 비교가능하게 환산 후 list화
    player_time = df1.swifter.apply(time_to_float, axis=1)
    player_time_list = player_time.to_list()

    # 수치상 비교위해 환산
    start_time = df3_start.swifter.apply(time_to_float, axis=1)
    start_time_list = start_time.to_list()

    end_time = df3_end.swifter.apply(time_to_float, axis=1)
    end_time_list = end_time.to_list()

    # 첫 페이즈의 하얀 원 중심좌표, 반지름 데이터를 df1에 추가하는 함수
    def add_gameStates_landing(row):

        safez_phases = [df3_phase['start_time'][i] for i in range(3, 16, 2)]
        safez_phase_times = [hours * 3600 + minutes * 60 + seconds for phase in safez_phases for hours, minutes, seconds in [map(float, phase.split(':'))]]

        whitecircle_location_x = df3[df3['_D'].str.contains(safez_phases[0])]['gameState.safetyZonePosition.x'].to_list()[0]
        whitecircle_location_y = df3[df3['_D'].str.contains(safez_phases[0])]['gameState.safetyZonePosition.y'].to_list()[0]
        whitecircle_radius = df3[df3['_D'].str.contains(safez_phases[0])]['gameState.safetyZoneRadius'].to_list()[0]
        
        return whitecircle_location_x, whitecircle_location_y, whitecircle_radius

    df1[['whitecircle_location_x', 'whitecircle_location_y', 'whitecircle_radius']] = df1.swifter.apply(add_gameStates_landing, axis=1, result_type='expand')

    df2[['whitecircle_location_x', 'whitecircle_location_y', 'whitecircle_radius']] = df2.swifter.apply(add_gameStates_landing, axis=1, result_type='expand')

    # 저장하기
    file_path_2 = f'C:/Users/PC/Desktop/AI_Lab/pubg/preprocessed/first_landing_location_{file_name}.csv'
    file_path_3 = f'C:/Users/PC/Desktop/AI_Lab/pubg/preprocessed/first_vehicle_location_{file_name}.csv'

    df1.to_csv(file_path_2, index=False)
    df2.to_csv(file_path_3, index=False)