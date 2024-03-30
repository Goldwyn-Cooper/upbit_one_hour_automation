import os
import requests

class TradingClient:
    def __init__(self):
        self.api_key = os.getenv('TRADING_API_KEY')
        if not self.api_key:
            raise ValueError('TRADING_API_KEY is not set')
        self.secret_key = os.getenv('TRADING_SECRET_KEY')
        if not self.secret_key:
            raise ValueError('TRADING_SECRET_KEY is not set')
        self.domain = os.getenv('TRADING_API_URL')
        if not self.domain:
            raise ValueError('TRADING_API_URL is not set')
    
    def get_balance(self):
        payload = dict(ak=self.api_key, sk=self.secret_key)
        response = requests.post(self.domain + '/account_balance',
                                 json=payload)
        response.raise_for_status()
        return response.json()
    
    def buy(self, ticker, amount):
        payload = dict(ak=self.api_key, sk=self.secret_key,
                       ticker=ticker, amount=amount)
        response = requests.post(self.domain + '/buy', json=payload)
        response.raise_for_status()
        return response.json()
    
    def sell(self, ticker, volume):
        payload = dict(ak=self.api_key, sk=self.secret_key,
                       ticker=ticker, volume=volume)
        response = requests.post(self.domain + '/sell', json=payload)
        response.raise_for_status()
        return response.json()
    
    def deposit(self, amount):
        payload = dict(ak=self.api_key, sk=self.secret_key, amount=amount)
        response = requests.post(self.domain + '/deposit', json=payload)
        response.raise_for_status()
        return response.json()
    
    def check_cash(self) -> float:
        balance : dict = self.get_balance()
        cash_balance : dict = balance.get('KRW', {})
        return float(cash_balance.get('balance', '0.0'))