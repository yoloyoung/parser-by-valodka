import asyncio
import websockets
import json
from all_array import *
import threading
import time
from bs4 import BeautifulSoup
import requests

async def getMain():
    for i in range(len(array)):
        try:
            response = f'wss://stream.binance.com:9443/stream?streams={array[i]}usdt@miniTicker'
            async with websockets.connect(response) as client:
                data = json.loads(await client.recv())['data']                                              
                responseTime = time.localtime(data['E'] // 1000)
                print('Назва монети ->', data['s'],'Час ->',f'{responseTime.tm_hour}:{responseTime.tm_min}:{responseTime.tm_sec}','Ціна за монету ->', data['c'],'Найнижча ціна за монету за 24 часа ->', data['l'],'Найвища ціна за монету за 24 часа ->', data['h'],'Обьем на площадкі ->', data['v'])
        except:
            print("Ты еблан, ты забанен")

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(getMain())
    
