import  time, threading, datetime
from bitstampy import api
from poloniex import Poloniex
import json
import requests
import csv
import gdax

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

wallet = 1000
payment = wallet

while wallet > 0:
	tickerGDAXETH_USD = public_client.get_product_ticker(product_id= 'ETH-USD')
	tickerGDAXLTC_USD = public_client.get_product_ticker(product_id= 'LTC-USD')

	GDAXETH_USD = float(tickerGDAXETH_USD['ask'])
	GDAXLTC_USD = float(tickerGDAXLTC_USD['ask'])

	BTSTLTC_USD = float(api.LTCUSD()['last'])
	BTSTETH_USD = float(api.ETHUSD()['last'])
	spreadGDAX_BS_LTC = (GDAXLTC_USD - BTSTLTC_USD) / GDAXLTC_USD
	spreadBS_GDAX_ETH = (BTSTETH_USD - GDAXETH_USD) / BTSTETH_USD
	totExch = spreadGDAX_BS_LTC + spreadBS_GDAX_ETH

		
	if totExch>.02:
		print spreadGDAX_BS_LTC
		Exchange = 'BTST_GDAX'
		print Exchange
		Instance = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
		wallet = wallet - payment
		time.sleep(600) #wait 30 seconds
		spreadGDAX_BS_LTC = (GDAXLTC_USD - BTSTLTC_USD) / GDAXLTC_USD
		Ret = payment * (1 + spreadGDAX_BS_LTC)
		time.sleep(300)
		spreadBS_GDAX_ETH = (BTSTETH_USD - GDAXETH_USD) / BTSTETH_USD
		Ret = Ret * (1 + spreadBS_GDAX_ETH)		
		wallet = wallet + Ret
		print Instance, Ret, wallet
		
		
	

