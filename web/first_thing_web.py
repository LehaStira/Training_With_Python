import requests
from re import findall
from datetime import datetime
from collections import Counter

ACCESS_TOKEN = '17da724517da724517da72458517b8abce117da17da72454d235c274f1a2be5f45ee711'

def get_json_data_from_url(url):
    my_res = requests.get(url).json()
    return my_res

def get_id_of_user(uid):
    url = f'https://api.vk.com/method/users.get?v=5.71&access_token={ACCESS_TOKEN}&user_ids={uid}'
    my_res = get_json_data_from_url(url)
    my_id = my_res['response'][0]['id']
    return my_id


def get_list_of_friends(id):
    url = f'https://api.vk.com/method/friends.get?v=5.71&access_token={ACCESS_TOKEN}&user_id={id}&fields=bdate'
    my_res = get_json_data_from_url(url)
    #print(my_res)
    return my_res


def get_count_of_friends(friends):
    return len(friends['response']['items'])


def get_list_of_dates(friends):
    list_of_dates = []
    print(friends)
    count_of_friends = get_count_of_friends(friends)
    for i in range(0,count_of_friends):
        try:
            list_of_dates.append(friends['response']['items'][i]['bdate'])
        except KeyError:
            pass
    return list_of_dates


def test_bool(date):
    tmp = findall('\d+', date)
    if len(tmp) == 3:
        return True
    else:
        return False


def filt(dates):
    dates = [i for i in dates if test_bool(i)]
    return dates


def get_year(date):
    tmp = findall('\d+', date)
    return tmp[2]


def get_years(dates):
    filter_dates = filt(dates)
    years = [get_year(i) for i in filter_dates]
    return years


def calculate_age(years):
    current_year = datetime.now().year
    list_of_ages = [current_year-int(year) for year in years]
    return list_of_ages


def get_result(ages):
    return Counter(ages).most_common(len(Counter(ages)))


def calc_age(uid):
    id_of_user = get_id_of_user(uid)
    list_of_friends = get_list_of_friends(id_of_user)
    list_of_dates = get_list_of_dates(list_of_friends)
    list_of_years = get_years(list_of_dates)
    list_of_ages = calculate_age(list_of_years)
    result = get_result(list_of_ages)
    return result


if __name__ == '__main__':
    res = calc_age('id158444621')
    print(res)