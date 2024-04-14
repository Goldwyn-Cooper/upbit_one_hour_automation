import os
import warnings
warnings.filterwarnings('ignore')
import requests
import pandas as pd

def get_default_info():
    BASE_ID = os.getenv('AIRTABLE_BASE_ID')  # Airtable의 베이스 ID
    TABLE_ID = os.getenv('AIRTABLE_TABLE_ID')  # Airtable의 테이블 ID
    TOKEN = os.getenv('AIRTABLE_TOKEN')  # Airtable의 토큰
    url = f'https://api.airtable.com/v0/{BASE_ID}/{TABLE_ID}'  # Airtable API의 URL
    headers = {'Authorization': f'Bearer {TOKEN}'}  # API 요청에 필요한 헤더
    return (url, headers)

def fetch_eth_info():
    url, headers = get_default_info() # 기본 정보를 가져옴
    
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    records = response.json().get('records')
    
    # 필요한 데이터 추출
    ids = map(lambda x: x.get('id'), records)
    data = map(lambda x: x.get('fields'), records)
    
    # 데이터프레임 생성
    df = pd.DataFrame(data)
    df.index = ids
    
    return df

def change_record(id, **kwargs):
    # 기본 정보 가져오기
    url, headers = get_default_info()
    
    # Airtable API URL에 id 추가
    url = f'{url}/{id}'
        
    # 업데이트할 데이터 생성
    data = {
        'fields': kwargs
    }
    
    # Airtable API를 통해 데이터 업데이트
    response = requests.patch(url, headers=headers, json=data)
    response.raise_for_status()

if __name__ == '__main__':
    from dotenv import load_dotenv
    load_dotenv()
    
    df = fetch_eth_info()
    print(df)