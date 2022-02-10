from all_array import *
from config import *
import sqlite3
async def getMain():   
    for i in range(len(array)):
        response = f'wss://stream.binance.com:9443/stream?streams=btcusdt@miniTicker'
        async with websockets.connect(response) as client:
            data = json.loads(await client.recv())['data']                                              
            responseTime = time.localtime(data['E'] // 1000)
            nameCoin = print('Назва монети ->', data['s'])
            dataCoin = print('Час ->',f'{responseTime.tm_hour}:{responseTime.tm_min}:{responseTime.tm_sec}')
            priceCoin = print('Ціна за монету ->', data['c'])
            lowerstPriceCoin = print('Найнижча ціна за монету за 24 часа ->', data['l'])
            highestPriceCoin = print('Найвища ціна за монету за 24 часа ->', data['h'])
            valueCoin = print('Обьем на площадкі ->', data['v'])
            database()
            
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(getMain())
