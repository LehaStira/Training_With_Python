from bs4 import BeautifulSoup
from decimal import Decimal
import requests


def get_soup(xml):
    soup = BeautifulSoup(xml, 'lxml')
    return soup


def get_hyper_text_valute(soup, kod):
    return soup.find('valute',
                     id=kod)


def get_nominal(soup, kod):
    hyper_text = get_hyper_text_valute(soup, kod)
    hyper_text_nominal = hyper_text.nominal
    res = hyper_text_nominal.text
    return res


def get_value(soup, kod):
    hyper_text = get_hyper_text_valute(soup, kod)
    hyper_text_value = hyper_text.value
    res = hyper_text_value.text
    return res


def get_course_of_exchange(value, nominal):
    return value/nominal


def _convert(amount, first_result, second_result):
    return amount / first_result * second_result


def convert(amount, cur_from, cur_to, date=None):
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

    my_xml = response.content

    soup = get_soup(my_xml)

    first_nominal = get_nominal(soup, cur_from)
    second_nominal = get_nominal(soup, cur_to)

    first_value = get_value(soup, cur_from)
    second_value = get_value(soup, cur_to)

    first_result = get_course_of_exchange(nominal = first_nominal,
                                          value = first_value)

    second_result = get_course_of_exchange(nominal = second_nominal,
                                           value = second_value)

    res = _convert(amount, first_result, second_result)
    res = str(res)

    result = Decimal(res)
    return result  # не забыть про округление до 4х знаков после запятой


if __name__ == "__main__":
    my_req = requests
