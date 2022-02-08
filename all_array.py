from bs4 import BeautifulSoup
import requests
array = [
'btc',
'eth',
'bnb',
'usdc',
'ada',
'sol',
'xrp',
'luna',
'dot',
'doge',
'avax',
'shib',
'busd',
'matic',
'ust',
'ltc',
'atom',
'link'
]
url = 'https://www.binance.com/uk-UA/markets/coinInfo'
responsible = requests.get(url).text
soup = BeautifulSoup(responsible, 'html.parser')
name_of_coin = soup.find_all("div", class_="css-1wp9rgv")
for item in name_of_coin:
	coins = print(item.text.lower())