from bs4 import BeautifulSoup
import unittest

from secong_solving import my_discr


def get_data(path):
    """
    Reading data from html file. Takes string path and
    return data from file.
    :param path:
    :return:
    """
    with open(path, 'r', encoding='utf-8') as f:
        res = f.read()
        return res


def get_soup(data):
    """
    Convert data of html file to soup
    :param data:
    :return:
    """
    my_soup = BeautifulSoup(data, 'lxml')
    return my_soup


def get_body(soup):
    """
    Takes body of soup from html file
    :param soup:
    :return:
    """
    res = soup.find('div', {'id' : 'bodyContent'})
    return res


def check_for_img(image):
    image.find()
    if image('data-file-width') != None:
        print(image.data_file_width)
        #if image('data-file-width') >= 200:
            #print(image) #
            #return True
    #return False



def get_imgs(body):
    """
    Return count of images with width >= 200
    :param body:
    :return:
    """
    print(type(body))
    imgs = body.find_all('img')
    my_im = [i for i in imgs if int(i['width']) >= 200]
    print(my_im)
    return len(my_im)


def get_h1(body):
    return body.find_all('h1')


def get_h2(body):
    return body.find_all('h2')


def get_h3(body):
    return body.find_all('h3')


def get_h4(body):
    return body.find_all('h4')


def get_h5(body):
    return body.find_all('h5')


def get_h6(body):
    return body.find_all('h6')


def bool_checking_h(el):
    print(f'Its el = {el}')
    main_thing = el.text[0]
    if main_thing == 'E' or main_thing == 'T' or main_thing == 'C':
        return True
    else:
        return False


def filter_h(all_h):
    print(f'its all_h = {all_h}')
    all_h = [i for i in all_h if bool_checking_h(i)]
    return all_h


def get_count_of_h(body):
    all_h1 = get_h1(body)
    all_h2 = get_h2(body)
    all_h3 = get_h3(body)
    all_h4 = get_h4(body)
    all_h5 = get_h5(body)
    all_h6 = get_h5(body)

    my_list = list()
    my_list.append(all_h1)
    my_list.append(all_h2)
    my_list.append(all_h3)
    my_list.append(all_h4)
    my_list.append(all_h5)
    my_list.append(all_h6)

    res = 0
    for ob in my_list:
        r = filter_h(ob)
        res += len(r)
    return res


def get_links_len()

def parse(path_to_file):
    # Поместите ваш код здесь.
    # ВАЖНО!!!
    # При открытии файла, добавьте в функцию open необязательный параметр
    # encoding='utf-8', его отсутствие в коде будет вызвать падение вашего
    # решения на грейдере с ошибк0ой UnicodeDecodeError
    data = get_data(path_to_file)
    soup = get_soup(data)
    body = get_body(soup)

    imgs = get_imgs(body)

    count = get_count_of_h(body)

    linkslen = get_links_len(body)

    return [imgs,count]
    #return [imgs, headers, linkslen, lists]


#class TestParse(unittest.TestCase):
#    def test_parse(self):
#        test_cases = (
#            ('wiki/Stone_Age', [13, 10, 12, 40]),
#            ('wiki/Brain', [19, 5, 25, 11]),
#            ('wiki/Artificial_intelligence', [8, 19, 13, 198]),
#            ('wiki/Python_(programming_language)', [2, 5, 17, 41]),
#            ('wiki/Spectrogram', [1, 2, 4, 7]),)

#        for path, expected in test_cases:
#            with self.subTest(path=path, expected=expected):
#                self.assertEqual(parse(path), expected)


if __name__ == '__main__':
    #unittest.main()
    my_path = 'C:\pythonProject\pythonProject\HowToMeetGirls\wiki\AI_winter'
    res = parse(my_path)
    print(res)
