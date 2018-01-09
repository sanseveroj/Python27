import  time, threading, datetime
from bitstampy import api
from poloniex import Poloniex
import json
import requests
import csv
import gdax
import hmac
import hashlib
import base64


def CheckTen(variable):
	t = threading.Timer(10.0, CheckTen)
	t.start()
	if variable >= 0:
		print variable
		t.cancel()
		return True

def BTSTGDAXTrader():
	x = threading.Timer(10.0, BTSTGDAXTrader)

	tickerGDAXETH_USD = public_client.get_product_ticker(product_id= 'ETH-USD')
	tickerGDAXLTC_USD = public_client.get_product_ticker(product_id= 'LTC-USD')

	GDAXETH_USD = float(tickerGDAXETH_USD['ask'])
	GDAXLTC_USD = float(tickerGDAXLTC_USD['ask'])

	BTSTLTC_USD = float(api.LTCUSD()['last'])
	BTSTETH_USD = float(api.ETHUSD()['last'])
	spreadGDAX_BS_LTC = (GDAXLTC_USD - BTSTLTC_USD) / GDAXLTC_USD
	spreadBS_GDAX_ETH = (BTSTETH_USD - GDAXETH_USD) / BTSTETH_USD
	totExch = spreadGDAX_BS_LTC + spreadBS_GDAX_ETH

	#BitStamp compared to Polo
	if totExch>.02:
		if BTST_LTCBal > 0:
			Exchange = 'BTST_GDAX'
			Instance = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
			print Exchange, Instance, spreadGDAX_BS_LTC
			api.litecoin_withdrawal(customer_id, api_key, api_secret).call(BTST_LTCBal, GDAX_Address)
			if CheckTen(GDAX_LTCBal):
				x.start()

#Bitstamp info
api_key = 'HP3Z2xOpvO7NLRM76earaNpAZWGtSyCK'
api_secret = 'd4owDCfbqZqjui7sVCfGzGrpSGpAVM70'
customer_id = 'oxnm1056'

#Bitstamp Message/Signature creation
nonce = int(time.time())
message = str(nonce) + customer_id + api_key
signature = hmac.new(
    api_secret,
    msg=message,
    digestmod=hashlib.sha256
).hexdigest().upper()


#Gdax Info
GDAX_Key = 'fb03a08dca90f0bbb77c09ae6090282c'
GDAX_Secret = base64.standard_b64decode('nQoLxU1N3ITM6QjMeeTpMWgZhsg5ossXp/AR6ySNuEH8npDyMRi4baw1CIvlWxk2+AclICLYivyisO/DEaXliw==')
GDAX_Pass = 'k1z4l7y3ia'

from requests.auth import AuthBase

# Create custom authentication for Exchange
class CoinbaseExchangeAuth(AuthBase):
    def __init__(self, api_key, secret_key, passphrase):
        self.api_key = GDAX_Key
        self.secret_key = GDAX_Secret
        self.passphrase = GDAX_Pass

    def __call__(self, request):
        timestamp = str(time.time())
        message = timestamp + request.method + request.path_url + (request.body or '')
        hmac_key = base64.b64decode(self.secret_key)
        signature = hmac.new(hmac_key, message, hashlib.sha256)
        signature_b64 = signature.digest().encode('base64').rstrip('\n')

        request.headers.update({
            'CB-ACCESS-SIGN': signature_b64,
            'CB-ACCESS-TIMESTAMP': timestamp,
            'CB-ACCESS-KEY': self.api_key,
            'CB-ACCESS-PASSPHRASE': self.passphrase,
            'Content-Type': 'application/json'
        })
        return request

api_url = 'https://api.gdax.com/'
auth = CoinbaseExchangeAuth(GDAX_Key, GDAX_Secret, GDAX_Pass)
auth_client = gdax.AuthenticatedClient(GDAX_Key, GDAX_Secret, GDAX_Pass)
print auth_client.get_account(GDAX_Pass)
exit()
# Get accounts
r = requests.get(api_url + 'accounts', auth=auth)
print r.json()
# [{"id": "a1b2c3d4", "balance":...

# Place an order
order = {
    'size': 1.0,
    'price': 1.0,
    'side': 'buy',
    'product_id': 'BTC-USD',
}
r = requests.post(api_url + 'orders', json=order, auth=auth)
print r.json()
# {"id": "0428b97b-bec1-429e-a94c-59992926778d"}


# Get accounts
r = auth_client.get_account(GDAX_Key)
print r
print 'finished'
exit()
# [{"id": "a1b2c3d4", "balance":...

### Place an order ###
#order = {
#    'size': 1.0,
#    'price': 1.0,
#    'side': 'buy',
#    'product_id': 'BTC-USD',
#}
#r = requests.post(api_url + 'orders', json=order, auth=auth)
#print r.json()
# {"id": "0428b97b-bec1-429e-a94c-59992926778d"}


public_client = gdax.PublicClient()

tickerGDAXETH_USD = public_client.get_product_ticker(product_id= 'ETH-USD')
tickerGDAXLTC_USD = public_client.get_product_ticker(product_id= 'LTC-USD')

GDAXETH_USD = float(tickerGDAXETH_USD['ask'])
GDAXLTC_USD = float(tickerGDAXLTC_USD['ask'])

BTSTLTC_USD = float(api.LTCUSD()['last'])
BTSTETH_USD = float(api.ETHUSD()['last'])
spreadGDAX_BS_LTC = (GDAXLTC_USD - BTSTLTC_USD) / GDAXLTC_USD
spreadBS_GDAX_ETH = (BTSTETH_USD - GDAXETH_USD) / BTSTETH_USD
totExch = spreadGDAX_BS_LTC + spreadBS_GDAX_ETH
print GDAXLTC_USD
print GDAXETH_USD
print BTSTLTC_USD
print BTSTETH_USD
print spreadGDAX_BS_LTC
print spreadBS_GDAX_ETH
print totExch

BTST_LTCBal = api.account_balancev2(customer_id, api_key, api_secret)['ltc_balance']

exit ()


					


			
			
		
	

