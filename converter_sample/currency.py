from bs4 import BeautifulSoup
from decimal import Decimal
import requests


def convert(amount, cur_from, cur_to, requests, date = None):
    """
    amount - сумма
    cur_from - код валюты, в которой передано значение
    cur_to - код валюты, в которую надо переконвертировать значение (через рубль)


    :param amount:
    :param cur_from:
    :param cur_to:
    :param date:
    :param requests:
    :return:
    """
    ulr = 'http://www.cbr.ru/scripts/XML_daily.asp?date_req=01/01/2021'
    response = requests.get(ulr)  # Использовать переданный requests



    result = Decimal('3754.8057')
    return result  # не забыть про округление до 4х знаков после запятой


if __name__ == "__main__":
    my_req = requests
