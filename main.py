def main():
    import requests
    from src.telegram import TelegramBot
    from src.trading import TradingClient
    from src.finance import Finance

    finance = Finance()
    client = TradingClient()
    bot = TelegramBot()
    candidate = 'BTC', 'ETH', 'SOL'

    try:
        bot.send_message('📌 UPBIT_1HOUR_AUTOMATION')
        balance = client.get_balance()
        total_balance = 0
        for ticker in list(candidate) + ['KRW']:
            if ticker not in balance:
                continue
            if ticker == 'KRW':
                total_balance += float(balance[ticker]['balance'])
                continue
            total_balance += float(
                balance[ticker]['balance']
            ) * finance.get_current_price(ticker)
        bot.send_message(f'💰 전체 잔고 : ₩{int(total_balance):,}')
        # print(total_balance)
        for ticker in candidate:
            print(f'[{ticker}]')
            if ticker in balance:
                asset_balance = float(balance[ticker]['balance'])
            else:
                asset_balance = 0
            max_budget = finance.max_ratio(ticker) * total_balance / len(candidate)
            current_price = finance.get_current_price(ticker)
            now_asset = asset_balance * current_price
            print(f'SCORE : {finance.get_score(ticker)}')
            print(f'AATR : {finance.get_aatr(ticker)}')
            if now_asset >= max_budget:
                print(f'🫨 최대 매수 금액 도달로 인한 청산 : {ticker}')
                bot.send_message(f'🫨 최대 매수 금액 도달로 인한 청산 : {ticker}')
                client.sell(ticker, asset_balance)
            elif finance.signal(ticker):
                print(f'🫡 20분할 매수 진행 : {ticker}')
                bot.send_message(f'🫡 20분할 매수 진행 : {ticker}')
                client.buy(ticker, max(5500, int(max_budget // 20)))
            elif not finance.signal(ticker) and asset_balance > 0:
                print(f'😱 하락 추세로 인한 청산 : {ticker}')
                bot.send_message(f'😱 하락 추세로 인한 청산 : {ticker}')
                client.sell(ticker, asset_balance)

    except requests.exceptions.HTTPError as e:
        print(e.response.status_code)
        print(e.response.reason)
    except Exception as e:
        print(type(e))
        print(e)
        bot.send_message(f'{type(e)}\n{e}')


if __name__ == '__main__':
    from dotenv import load_dotenv

    load_dotenv()
    import warnings

    warnings.filterwarnings('ignore')
    main()
