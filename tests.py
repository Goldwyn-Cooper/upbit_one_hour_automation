from unittest import TestCase, main, skip
import os
import warnings
import logging
warnings.filterwarnings('ignore')
logging.basicConfig(level=logging.WARNING)

import requests
import pandas as pd

from src.trading import TradingClient

class FinanceTests(TestCase):
    def test_get_price(self):
        from src.finance import Finance
        finance = Finance()
        price = finance.get_price('BTC')
        self.assertIsInstance(price, pd.DataFrame)
    
    def test_get_score(self):
        from src.finance import Finance
        finance = Finance()
        score = finance.get_score('BTC')
        self.assertIsInstance(score, float)
    
    def test_get_aatr(self):
        from src.finance import Finance
        finance = Finance()
        aatr = finance.get_aatr('BTC')
        self.assertIsInstance(aatr, float)

    def test_get_current_price(self):
        from src.finance import Finance
        finance = Finance()
        current_price = finance.get_current_price('BTC')
        self.assertIsInstance(current_price, float)
    
    def test_signal(self):  
        from src.finance import Finance
        finance = Finance()
        finance.signal('BTC')
    
    def test_max_ratio(self):
        from src.finance import Finance
        finance = Finance()
        max_ratio = finance.max_ratio('BTC')
        self.assertIsInstance(max_ratio, float)

class TradingTests(TestCase):
    def test_api_key(self):
        api_key = os.getenv("TRADING_API_KEY")
        self.assertIsInstance(api_key, str)

    def test_secret_key(self):
        secret_key = os.getenv("TRADING_SECRET_KEY")
        self.assertIsInstance(secret_key, str)

    def test_domain(self):
        domain = os.getenv("TRADING_API_URL")
        self.assertIsInstance(domain, str)

    # @skip("Do not need to test")
    def test_get_balance(self):
        client = TradingClient()
        balance = client.get_balance()
        # print(balance)
        self.assertIsInstance(balance, dict)
    
    def test_buy_ticker_error(self):
        client = TradingClient()
        with self.assertRaises(requests.exceptions.HTTPError):
            client.buy('BBTTCC', 1000)
    
    def test_buy_amount_error(self):
        client = TradingClient()
        with self.assertRaises(requests.exceptions.HTTPError):
            client.buy('BTC', 1000)
    
    def test_sell_ticker_error(self):
        client = TradingClient()
        with self.assertRaises(requests.exceptions.HTTPError):
            client.sell('BBTTCC', 1000)
    
    def test_sell_volume_error(self):
        client = TradingClient()
        with self.assertRaises(requests.exceptions.HTTPError):
            client.sell('BTC', 1000)

class TelegramTests(TestCase):
    def test_bot_token(self):
        bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
        self.assertIsInstance(bot_token, str)

    def test_chat_id(self):
        chat_id = os.getenv("TELEGRAM_CHAT_ID")
        self.assertIsInstance(chat_id, str)

    @skip("Do not need to test")
    def test_send_message(self):
        from src.telegram import TelegramBot

        bot = TelegramBot()
        bot.send_message("📌 UPBIT_1HOUR_AUTOMATION")


if __name__ == "__main__":
    from dotenv import load_dotenv

    load_dotenv()
    main()
