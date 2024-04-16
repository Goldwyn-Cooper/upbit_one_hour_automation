import warnings
warnings.filterwarnings('ignore')

import requests
import pandas as pd
from src.airtable import fetch_eth_info, change_record
from src.trading import TradingClient
from src.dt import get_now_text

def main():
    df = fetch_eth_info()
    tc = TradingClient()
    data = tc.get_deposit_list('KRW', df.iloc[0]['DT'])
    df_dl = pd.DataFrame(data)
    df_dl.amount = df_dl.amount.astype(float)
    # print(df_dl)
    krw = int(df_dl['amount'].sum())
    # print(krw)
    data = tc.get_withdraw_list('ETH', df.iloc[0]['DT'])
    df_wl = pd.DataFrame(data)
    df_wl.amount = df_wl.amount.astype(float)
    # print(df_wl)
    eth_staking = round(df_wl['amount'].sum() * 100_000_000) / 100_000_000
    # print(eth_staking)
    # print(tc.get_balance())
    eth_balance = float(tc.get_balance()['ETH']['balance'])
    # print(eth_balance)
    eth_price = int(float(requests.get('https://api.upbit.com/v1/ticker',
                             params={'markets': 'KRW-ETH'}).json()[0]['trade_price']))
    # print(eth_price)
    id = df.index[0]
    # print(id)
    ud = dict(KRW=int(df.iloc[0]['KRW']) + int(krw),
              Staking=float(df.iloc[0]['Staking']) + eth_staking,
              Cash=tc.check_cash(),
              Balance=eth_balance,
              Price=eth_price)
    print(ud)
    change_record(id,
                  DT=get_now_text('%Y-%m-%d %H:%M:%S+09:00'),
                  **ud)

if __name__ == '__main__':
    from dotenv import load_dotenv

    load_dotenv()
    main()