import warnings
warnings.filterwarnings('ignore')
from src.trading import TradingClient
from src.telegram import TelegramBot
from src.gh import make_github_issue
from src.dt import get_now_text

def main():
    client = TradingClient()
    bot = TelegramBot()
    # 잔고를 조회한다
    cash_val = client.check_cash()
    # 잔고가 20020원 미만이면 입금을 시도한다
    MIN_CASH = 20020
    if cash_val >= MIN_CASH: return
    # 입금을 시도했다는 것을 이슈로 남긴다
    amount = max(5000, int(MIN_CASH - cash_val) + 1)
    client.deposit(amount)
    # 입금을 시도했다는 것을 이슈로 남긴다
    make_github_issue(f'입금 시도 ({get_now_text()})', f'부족한 금액의 입금을 시도했습니다!')
    bot.send_message('📌 UPBIT_1HOUR_AUTOMATION')
    msg = f'부족한 금액의 입금을 시도합니다.\n'
    msg += f'- 현재금액: ₩{int(cash_val):,}\n'
    msg += f'- 필요금액: ₩{amount:,}'
    bot.send_message(msg)

if __name__ == '__main__':
    main()