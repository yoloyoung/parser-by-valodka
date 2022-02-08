from main import *
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
#Берём Url сайта
url = 'https://www.binance.com/uk-UA/markets/coinInfo'
#Забираем Названия Монет
responsible = requests.get(url).text
soup = BeautifulSoup(responsible, 'html.parser')
nameOfCoin = soup.find_all("div", class_="css-1wp9rgv")
for item in nameOfCoin:
	coins = print(item.text.lower())
