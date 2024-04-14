from time import sleep
import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import pyupbit
from src.trading import TradingClient
from src.telegram import TelegramBot
from src.gh import make_github_issue
from src.dt import get_now_text

def main():
    client = TradingClient()
    bot = TelegramBot()
    # 잔고를 조회한다
    cash_val = client.check_cash()
    # 잔고가 10010원 미만이면 매수 실패 처리하고 이슈 및 메시지를 남긴다
    MIN_CASH = 10010
    if cash_val < MIN_CASH:
        header = f'매수 실패 ({get_now_text()})'
        body = '금액이 부족해 매수할 수 없습니다!'
        make_github_issue(header, body)
        bot.send_message('📌 UPBIT_1HOUR_AUTOMATION')
        msg = '금액이 부족해 매수할 수 없습니다!\n'
        msg += f'- 현재금액: ₩{int(cash_val):,}\n'
        msg += f'- 필요금액: ₩{int(MIN_CASH - cash_val) + 1:,}'
        bot.send_message(msg)
        return
    # 비트코인과 이더리움을 매수한다
    # client.buy('BTC', 5000)
    # client.buy('ETH', 5000)
    client.buy('ETH', 10000) # 이더 매수 
    # 매수를 시도했다는 것을 이슈로 남긴다
    print('Wait 5 seconds...')
    sleep(5)
    # df = pd.DataFrame(client.get_balance()).T
    # df = df.loc[['BTC', 'ETH'], ['avg_buy_price']]
    # df['current_price'] = [pyupbit.get_current_price(f'KRW-{ticker}')
    #                        for ticker in df.index]
    # df.avg_buy_price = df.avg_buy_price.map(float).map(int)
    # df.current_price = df.current_price.map(int)
    # df['rate'] = ((df.current_price - df.avg_buy_price)
    #               / df.avg_buy_price * 100).round(2)
    # df.columns = ['매수평균가', '현재가', '수익률']
    bot.send_message('📌 UPBIT_1HOUR_AUTOMATION')
    # msg = '비트코인과 이더리움을 매수했습니다!\n\n'
    msg = '이더리움을 매수했습니다!'
    # msg += df.to_string()
    bot.send_message(msg)
    header = f'매수 성공 ({get_now_text()})'
    # body = '비트코인과 이더리움을 매수했습니다!\n\n'
    # body += df.astype(str).to_markdown()
    make_github_issue(header, msg)

if __name__ == '__main__':
    main()