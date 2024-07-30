from django.shortcuts import render, redirect
from .kevin_client import KevinAPIClient

def choose_bank(request):
    client = KevinAPIClient()
    banks = client.get_banks().get('data', [])
    return render(request, 'payment/choose_bank.html', {'banks': banks})

def initiate_payment(request, bank_id):
    client = KevinAPIClient()
    payment_data = {
        'amount': '10.00',  # Pakeiskite pagal realią sumą
        'currencyCode': 'EUR',
        'bankId': bank_id,
        'redirectUrl': 'https://your-site.com/payment-return/',
        'webhookUrl': 'https://your-site.com/payment-webhook/',
    }
    response = client.initiate_payment(payment_data)
    return redirect(response.get('confirmationUrl'))
