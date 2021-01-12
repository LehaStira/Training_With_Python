from re import findall


class Solving:
    def __init__(self, string_task, method_of_solving):
        self.my_task = string_task
        self.method_of_solving = method_of_solving

    my_task = property()
    method_of_solving = property()

    @method_of_solving.getter
    def method_of_solving(self):
        if self.solve == 0:
            return 'Дискриминант'
        elif self.solve == 1:
            return 'Теорема Виетта'

    @method_of_solving.setter
    def method_of_solving(self, value):
        if value == 'Дискриминант':
            self.solve = 0
        elif value == 'Теорема Виетта':
            self.solve = 1
        else:
            raise ValueError('Неверно указанный метод решения. Валидные значения: Дискриминант, Теорема Виетта')

    @my_task.setter
    def my_task(self, value):
        if isinstance(value, str):
            if '=' in value:
                self._string_task = value
        else:
            self._string_task = None

    @my_task.getter
    def my_task(self):
        return self._string_task

    def _solve_by_discr(self):
        my_list = self.get_three_decimals()
        a, b, c = int(my_list[0]), int(my_list[1]), int(my_list[2])
        d = (b * b) - (4 * a * c)
        if (d ** 1 / 2) % 1 != 0:
            ValueError("Нет корней!")
        x1 = (-b - d ** 1 / 2) // (2 * a)
        x2 = (-b + d ** 1 / 2) // (2 * a)
        res = (x1, x2)
        return res

    def _solve_by_viett(self):
        print('Формула решена Виеттом. Честно. Нет.')
        my_list = self.get_three_decimals()
        a, b, c = int(my_list[0]), int(my_list[1]), int(my_list[2])
        my_res = self._solve_by_discr(a, b, c)
        return my_res

    def solving(self):
        if self.solve == 0:
            res = self._solve_by_discr()
        else:
            res = self._solve_by_viett()
        return res

    def get_three_decimals(self):
        return findall('\d+', self.my_task)


def get_kind_of_solving():
    my_kind = input('Укажите метод решения: (Варианты - Теорема Виетта, Дискриминант) ')
    if my_kind == 'Теорема Виетта' or my_kind == 'Дискриминант':
        return my_kind
    else:
        raise ValueError


def get_user_equation():
    user_task = input('Введите уравнение: ')
    return user_task


def main():
    user_task = get_user_equation()
    kind_of_solving = get_kind_of_solving()
    my_solve = Solving(user_task, kind_of_solving)
    res = my_solve.solving()
    print(res)


if __name__ == '__main__':
    main()