import asyncio
import logging

import aiohttp
import configargparse
from bs4 import BeautifulSoup
import requests

import time



class ParseIni:
    def __init__(self):
        parser = configargparse.ArgParser()
        parser.add_argument('-c, --config', default='config.ini', is_config_file=True,
                            help='Path to file config.ini')
        parser.add_argument('--currency_source',
                            default='http://www.finmarket.ru/currency/USD/',
                            help='Currency web-source')
        parser.add_argument('--sleep', default=3,
                            help='Update delay in seconds')
        parser.add_argument('--tracking_point', default=0.5,
                            help='Change rate point')
        parser.add_argument('--headers', default={'User-Agent': 'Mozilla/5.0'},
                            help='Change rate point')
        parser.add_argument('--log_config',
                            default={"level": logging.INFO,
                                     "format": "%(asctime)s %(levelname)s %(message)s",
                                     "filename": "logger.log"},
                            help='Log configs')
        args = parser.parse_args()
        self.currency_source = args.currency_source
        self.sleep = args.sleep
        self.tracking_point = args.tracking_point
        self.headers = args.headers
        self.log_config = args.log_config
async def fun1(x):
    print(x**2)
    await asyncio.sleep(4)
    print('fun1 завершена')


async def fun2(x):
    print(x**0.5)
    await asyncio.sleep(0)
    print('fun2 завершена')

async def get_currency_price( currency_source, headers):
    async with aiohttp.ClientSession() as session:
        full_page = await session.get(url=currency_source)
    print('-------------')
    # full_page = requests.get(currency_source)
    # {'headers': headers})
    print(full_page.headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll("div", {"class": "valvalue"})
    print(convert[0].text)
    return convert[0].text

async def main():
    task1 = asyncio.create_task(fun1(4))
    task2 = asyncio.create_task(fun2(4))
    task3 = asyncio.create_task(get_currency_price(used_args.currency_source, used_args.headers))

    await task1
    await task2
    await task3

if __name__=='__main__':
    used_args = ParseIni()
    # print(get_currency_price(used_args.currency_source, used_args.headers))
    print(time.strftime('%X'))

    asyncio.run(main())

    print(time.strftime('%X'))