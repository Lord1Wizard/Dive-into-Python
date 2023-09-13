import configargparse
import asyncio
import requests
from bs4 import BeautifulSoup
import logging
import json
import sys


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


class Currency:

    def __init__(self, currency_source, headers, tracking_point):
        self.currency_source = currency_source
        self.headers = headers
        self.tracking_point = tracking_point
        self.loop = asyncio.get_event_loop()
        self.start_flag = 0
        self.starting_currency = None

    async def get_currency_price(self):
        """Парсинг сайта"""
        full_page = await self.loop.run_in_executor(None, requests.get,
                                                    self.currency_source,
                                                    {'headers': self.headers})
        soup = BeautifulSoup(full_page.content, 'html.parser')
        convert = soup.findAll("div", {"class": "valvalue"})
        return convert[0].text

    async def check_currency(self, logger):
        """Проверка изменения курса валюты и логирование"""
        while self.start_flag:
            currency = await self.get_currency_price()
            currency = float(currency.replace(",", "."))
            if self.starting_currency is None:
                logger.warning("Start! Current currency value: %f", currency)
                self.starting_currency = currency
            if currency >= self.starting_currency + float(
                    self.tracking_point):
                logger.warning(
                    "The course has grown a lot! Current currency value: %f",
                    currency)
            elif currency <= self.starting_currency - float(
                    self.tracking_point):
                logger.warning(
                    "The course has dropped a lot! Current currency value: %f",
                    currency)
            self.starting_currency = currency
            logger.info(f'{self.starting_currency}')


async def waiting_input():
    """Ожидания ввода команды"""
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, input, 'Enter command:\n')


async def main():
    # Загрузка параметров программы из ini файла
    used_args = ParseIni()
    json_data = json.loads(used_args.log_config)
    # Логирование в файл
    logger = logging.getLogger(__name__)
    logger.setLevel(json_data['level'])
    handler = logging.FileHandler(f'{json_data["filename"]}', mode='a')
    formatter = logging.Formatter(json_data['format'])
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    # Логирование на экран
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setLevel(logging.WARNING)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    logger.info(used_args.log_config)
    current_currency = Currency(used_args.currency_source, used_args.headers, used_args.tracking_point)
    start = None
    temp = None
    while True:
        if start == "Currency":
            current_currency.start_flag = 1
            temp = asyncio.gather(current_currency.check_currency(logger))
        elif start == 'Price':
            print(current_currency.starting_currency)
        elif start == 'Exit':
            current_currency.start_flag = 0
            try:
                await temp
            except Exception as e:
                print('Логирование не было запущено', e)
            break
        elif start:
            pass
        else:
            print('Такой команды нет\nСписок команд:\nCurrency - запуск отслеживания курса валюты и логирования'
                  '\nPrice - текущее значение курса\nExit - выход')
        start = await waiting_input()


if __name__ == "__main__":
    asyncio.run(main())
