#library
import pandas as pd
from datetime import datetime
import swifter

def character_processing(file_name):

    file_path = f'C:/Users/PC/Desktop/AI_Lab/pubg/data/{file_name}.csv'

    #파일 불러오기
    df = pd.read_csv(file_path)

    #필요한 컬럼별로 dataframe 구성
    df1=df[['_D','character.name', 'character.location.x', 'character.location.y', 'character.location.z','character.isInBlueZone']]
    df2=df[['_D', 'common.isGame', 'gameState.safetyZoneRadius','gameState.safetyZonePosition.x', 'gameState.safetyZonePosition.y', 'gameState.safetyZonePosition.z']]

    #저장진행
    df1.to_csv(r'C:\Users\PC\Desktop\AI_Lab\pubg\tel_processing\character.csv', index=False)
    df2.to_csv(r'C:\Users\PC\Desktop\AI_Lab\pubg\tel_processing\gameState.csv', index=False)

    #전처리
    df1 = df1.dropna()
    df2 = df2.dropna()

    #_D 시간데이터 정규표현식으로 전처리
    df1['_D'] = pd.to_datetime(df1['_D']).dt.strftime('%H:%M:%S.%f').str[:-3]
    df2['_D'] = pd.to_datetime(df2['_D']).dt.strftime('%H:%M:%S.%f').str[:-3]

    df2_sample = df2[['_D','common.isGame','gameState.safetyZoneRadius']]

    df2_start = df2_sample.drop_duplicates('common.isGame', keep='first')
    df2_end = df2_sample.drop_duplicates('common.isGame', keep='last')

    # df2_start, end 값 비교하여 볼수 있도록 df2_phase 구성
    df2_phase = pd.merge(df2_start, df2_end, on='common.isGame')
    df2_phase = df2_phase[['common.isGame','_D_x','_D_y']]

    df2_phase.columns = ['phase','start_time','end_time']

    # _D값 비교가능하게 float화하는 함수
    def time_to_float(row):
        time_data = row['_D']
        hours, minutes, seconds = map(float, time_data.split(':'))
        time_data = hours * 3600 + minutes * 60 + seconds

        return  time_data

    # 선수별 시간 데이터 : 수치상 비교가능하게 환산 후 list화
    player_time = df1.swifter.apply(time_to_float, axis=1)
    player_time_list = player_time.to_list()

    # 수치상 비교위해 환산
    start_time = df2_start.swifter.apply(time_to_float, axis=1)
    start_time_list = start_time.to_list()

    end_time = df2_end.swifter.apply(time_to_float, axis=1)
    end_time_list = end_time.to_list()

    # 방법 2 진행전 낙하위치 및 시간 산출 위해 df3 구성
    df3=df[['_D','character.name', 'character.location.x', 'character.location.y', 'character.location.z','item.itemId']]

    df3 = df3.dropna()
    df3['_D'] = pd.to_datetime(df3['_D']).dt.strftime('%H:%M:%S.%f').str[:-3]

    # 낙하산만 사용한 값만 나오게 처리
    df3 = df3[df3['item.itemId'] == 'Item_Back_B_01_StartParachutePack_C']

    # item.itemId는 equip, unequip 총 2번씩 log가 남음
    # 마지막 데이터만 남게하면 착지한 시점 및 시간 알 수 있음
    df3 = df3.drop_duplicates(subset='character.name', keep='last')

    # 낙하시점 : 수치상 비교가능하게 환산 후 list화
    landing_time = df3.swifter.apply(time_to_float, axis=1)
    landing_time_list = landing_time.to_list()

    # prephase 제거하는 함수

    def delete_prephase(row):
        player_time = row['_D']
        player_name = row['character.name']
        hours, minutes, seconds = map(float, player_time.split(':'))
        player_time = hours * 3600 + minutes * 60 + seconds
        
        landing_time = df3[df3['character.name'].str.contains(player_name)]['_D'].to_list()[0]
        hours, minutes, seconds = map(float, landing_time.split(':'))
        landing_time = hours * 3600 + minutes * 60 + seconds

        for name in df3['character.name']:
            if name == row['character.name']:
                return player_time >= landing_time
            
    df1 = df1[df1.swifter.apply(delete_prephase,axis=1)]


    # 선수별 시간값과 페이즈별 시작시간 값을 비교하여 phase, 하얀 원 중심좌표, 반지름 데이터를 df1에 추가하는 함수
    def add_gameStates(row):

        player_time = row['_D']
        hours, minutes, seconds = map(float, player_time.split(':'))
        player_time = hours * 3600 + minutes * 60 + seconds

        safez_phases = [df2_phase['start_time'][i] for i in range(3, 16, 2)]
        safez_phase_times = [hours * 3600 + minutes * 60 + seconds for phase in safez_phases for hours, minutes, seconds in [map(float, phase.split(':'))]]

    
        # 예) 2페이즈 start_time 시간 이전 선수 위치는 아직 1페이즈 진행중이라 할 수 있음
        #     이는 phase = 1.0, 1페이즈의 하얀 원 중심좌표 및 반지름 = 2페이즈의 페이즈 준비시간시 정지해있는 원의 좌표 및 반지름 의미
        # 위 내용을 바탕으로 1페이즈, 2페이즈, ... 7페이즈 계산함
        for i in range(0,len(safez_phase_times)):
            if player_time <= safez_phase_times[i]:
                phase = float(df2[df2['_D'].str.contains(safez_phases[i])]['common.isGame'].to_list()[0])-1.0
                whitecircle_location_x = df2[df2['_D'].str.contains(safez_phases[i])]['gameState.safetyZonePosition.x'].to_list()[0]
                whitecircle_location_y = df2[df2['_D'].str.contains(safez_phases[i])]['gameState.safetyZonePosition.y'].to_list()[0]
                whitecircle_radius = df2[df2['_D'].str.contains(safez_phases[i])]['gameState.safetyZoneRadius'].to_list()[0]

                return phase, whitecircle_location_x, whitecircle_location_y, whitecircle_radius

        # 이후 기준 하얀원 값이 없지만, 어차피 원이 작아서 마지막 phase data로 대신 설정    
        if player_time > safez_phase_times[6]:
            phase = float(df2[df2['_D'].str.contains(safez_phases[6])]['common.isGame'].to_list()[0])-1.0
            whitecircle_location_x = df2[df2['_D'].str.contains(safez_phases[6])]['gameState.safetyZonePosition.x'].to_list()[0]
            whitecircle_location_y = df2[df2['_D'].str.contains(safez_phases[6])]['gameState.safetyZonePosition.y'].to_list()[0]
            whitecircle_radius = df2[df2['_D'].str.contains(safez_phases[6])]['gameState.safetyZoneRadius'].to_list()[0]

            return phase, whitecircle_location_x, whitecircle_location_y, whitecircle_radius
        
    df1[['phase', 'whitecircle_location_x', 'whitecircle_location_y', 'whitecircle_radius']] = df1.swifter.apply(add_gameStates, axis=1, result_type='expand')

    # 저장하기
    file_path_2 = f'C:/Users/PC/Desktop/AI_Lab/pubg/preprocessed/character_location_{file_name}.csv'

    df1.to_csv(file_path_2, index=False)