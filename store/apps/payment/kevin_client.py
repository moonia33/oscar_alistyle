import requests
import base64

class KevinAPIClient:
    BASE_URL = 'https://api.kevin.eu/platform/v0.3'
    CLIENT_ID = '68cb5316-0318-4ed6-a567-e9758c98f711'
    CLIENT_SECRET = '7d42b109938bc826c111c606903b96d38225334e0d0738b18a93c57fe92df1d3'
    ENDPOINT_SECRET = '27358fe3-378b-4b42-971a-cbbfe93b4c4d'

    def __init__(self):
        self.access_token = self.get_access_token()

    def get_access_token(self):
        url = f'{self.BASE_URL}/auth/token'
        auth_string = f"{self.CLIENT_ID}:{self.CLIENT_SECRET}"
        auth_encoded = base64.b64encode(auth_string.encode('utf-8')).decode('utf-8')
        headers = {
            'Authorization': f'Basic {auth_encoded}',
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        data = {'grant_type': 'client_credentials'}
        response = requests.post(url, headers=headers, data=data)
        response.raise_for_status()
        return response.json()['access_token']

    def get_headers(self):
        return {
            'Authorization': f'Bearer {self.access_token}',
            'Accept': 'application/json',
        }

    def get_banks(self):
        url = f'{self.BASE_URL}/auth/banks'
        headers = self.get_headers()
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

    def initiate_payment(self, payment_data):
        url = f'{self.BASE_URL}/payment/initiate'
        headers = self.get_headers()
        response = requests.post(url, headers=headers, json=payment_data)
        response.raise_for_status()
        return response.json()
