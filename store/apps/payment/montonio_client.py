import jwt
import requests
from datetime import datetime, timedelta, timezone

class MontonioAPIClient:
    BASE_URL = 'https://sandbox-stargate.montonio.com/api'
    ACCESS_KEY = 'a6e99fdc-4f53-4aba-825e-b26b723f9448'
    SECRET_KEY = 'A3a6hFc6LvXjaIPoDSFYhndHPakuI/1edwTSw1kIiY1v'

    def __init__(self):
        self.access_token = self.generate_access_token()

    def generate_access_token(self):
        payload = {
            'accessKey': self.ACCESS_KEY,
            'iat': datetime.now(timezone.utc),
            'exp': datetime.now(timezone.utc) + timedelta(hours=1)
        }
        token = jwt.encode(payload, self.SECRET_KEY, algorithm='HS256')
        return token

    def get_headers(self):
        return {
            'Authorization': f'Bearer {self.access_token}',
            'Accept': 'application/json',
        }

    def get_payment_methods(self):
        url = f'{self.BASE_URL}/stores/payment-methods'
        response = requests.get(url, headers=self.get_headers())
        response.raise_for_status()
        return response.json()

    def create_order(self, order_data):
        url = f'{self.BASE_URL}/orders'
        response = requests.post(url, headers=self.get_headers(), json=order_data)
        response.raise_for_status()
        return response.json()
