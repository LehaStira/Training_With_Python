from bs4 import BeautifulSoup
from decimal import Decimal
import requests
from pprint import pprint


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
    # код валюты находится в CharCode

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
    print('Мы получили xml, выглядит как-то так:')
    print()
    pprint(my_xml)
    print()
    print()
    soup = get_soup(my_xml)

    print('get_soup отработал, получили суп, выглядит как-то так: ')
    print()
    pprint(soup)
    print()
    print()
    first_nominal = get_nominal(soup, cur_from)
    second_nominal = get_nominal(soup, cur_to)

    print('Функция get_nominal отработала дважды')
    print()
    print(f'first_nominal = {first_nominal}')
    print(f'second_nominal = {second_nominal}')
    print()
    print()

    first_value = get_value(soup, cur_from)
    second_value = get_value(soup, cur_to)

    print('Функция get_value отработала дважды')
    print()
    print(f'first_value = {first_value}')
    print(f'second_value = {second_value}')
    print()
    print()
    first_result = get_course_of_exchange(nominal = first_nominal,
                                          value = first_value)

    print('Функция get_course_of_exchange отработала 1 раз')
    print()
    print(f'first_result = {first_result}')
    print()
    print()

    second_result = get_course_of_exchange(nominal = second_nominal,
                                           value = second_value)

    print('Функция get_course_of_exchange отработала 2 раз')
    print()
    print(f'second_result = {second_result}')
    print()
    print()
    res = _convert(amount, first_result, second_result)
    print('Функция _convert отработала')
    print(f'res = {res}')
    res = str(res)

    result = Decimal(res)
    return result  # не забыть про округление до 4х знаков после запятой


if __name__ == "__main__":
    my_req = requests
