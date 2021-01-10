from re import findall


def get_kind_of_solving():
    my_kind = input('Укажите метод решения: (Варианты - Теорема Виетта, Дискриминант) ')
    if my_kind == 'Теорема Виетта' or my_kind == 'Дискриминант':
        return my_kind
    else:
        raise ValueError


def get_user_equation():
    user_task = input('Введите уравнение: ')
    return user_task


def get_koef(user_task):
    return findall('\d+', user_task)


def my_viett(a,b,c):
    """
    Solving by Viett
    :param a:
    :param b:
    :param c:
    :return:
    """
    print('Формула решена Виеттом. Честно. Нет.')
    my_res = my_discr(a,b,c)
    return my_res


def my_discr(a,b,c):
    d = (b*b) - (4*a*c)
    if (d ** 1/2) % 1 != 0:
        ValueError("Нет корней!")
    x1 = (-b - d ** 1/2) // (2*a)
    x2 = (-b + d ** 1/2) // (2*a)
    res = (x1, x2)
    return res

def solving(a,b,c,kind):
    if kind == 'Теорема Виетта':
        res = my_viett(a,b,c)
    else:
        res = my_discr(a,b,c)
    return res

def main():
    user_task = get_user_equation()
    kind_of_solving = get_kind_of_solving()
    my_koef = get_koef(user_task)
    a = int(my_koef[0]) #5*x*x+4*x+3=0
    b = int(my_koef[1])
    c = int(my_koef[2])
    res = solving(a,b,c,kind_of_solving)

    print(f'x1 = {res[0]}, x2 = {res[1]}')


if __name__ == '__main__':
    main()