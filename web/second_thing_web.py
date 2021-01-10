import re


def calculate(data, findall):
    matches = findall(r"", data)  # Если придумать хорошую регулярку, будет просто
    for v1, s, v2, n in matches:  # Если кортеж такой структуры: var1, [sign]=, [var2], [[+-]number]
        # Если бы могло быть только =, вообще одной строкой все считалось бы, вот так:
        data[v1] = data.get(v2, 0) + int(n or 0)

    return data


def get_text_of_file(path):
    with open(path, 'r') as f:
        res = f.read()
        return res


if __name__ == '__main__':
    my_findall = re.findall
    my_data = get_text_of_file('test_second.txt')
    res = calculate(data = my_data,
                    findall = my_findall)
    print(res)
