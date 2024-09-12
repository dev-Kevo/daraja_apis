import requests
from requests.auth import HTTPBasicAuth
import os
from dotenv import load_dotenv
import datetime
import base64
from .utils import mpesa_response

load_dotenv()


# variables
consumer_key = os.getenv('CONSUMER_KEY')
consumer_secret = os.getenv('CONSUMER_SECRET')
pass_key = os.getenv('PASSKEY')
business_short_code = os.getenv('BUSINESS_SHORT_CODE')

#step number 1
def get_access_token(consumer_key: str = None, consumer_secret: str = None):
    """
    Make a call to daraja TO GET Acess to the APIs

    return: Access token
    """
    request_url = 'https://api.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
    headers = {'Content-Type' : 'application/json'}
    auth = (consumer_key, consumer_secret)

    try:
        response = requests.get(request_url, headers=headers, auth=auth)
        
        return response.json()['access_token']
    except Exception as e:
        return f'Error {e}'

def stkpush(phone_number: str):
    """
    [ -- POST REQUEST -- ]
    Automate M-pesa payments
    params:
        - Phone number
    """

    push_url = 'https://api.safaricom.co.ke/mpesa/stkpush/v1/processrequest'

    timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    password = base64.b64encode((business_short_code + pass_key + timestamp).encode('ascii')).decode('utf-8')
    transction_type = 'CustomerPayBillOnline'

    payload = {
        'BusinessShortCode' : business_short_code,
        'Password' : password,
        'Timestamp' : timestamp,
        'TransactionType' : transction_type,
        'Amount' : 20,
        'PartyA' : phone_number,
        'PartyB' : business_short_code,
        'PhoneNumber' : phone_number,
        'CallBackURL' : 'https://api.darajambili.com/express-payment',
        'AccountReference' : 'Test',
        'TransactionDesc' : 'Some cool description'

    }


    headers = {
        'Authorization' : 'Bearer ' + get_access_token(consumer_key=consumer_key, consumer_secret=consumer_secret),
        'Content-Type' : 'application/json'
    }

    try:
        res = requests.post(url=push_url, json=payload, headers=headers)
        response = mpesa_response(res)
        return response.json()
    
    except Exception as e:
        return f"Error: {e}"
    


    







