class MyClass:
    def __init__(self, a):
        self.real_a = a

    real_a = property()

    @real_a.getter
    def real_a(self):
        return self._a

    @real_a.setter
    def real_a(self, value):
        if value > 0:
            self._a = value
        else:
            raise ValueError('Значение а меньше нуля!')

    def __str__(self):
        return f'Значение а в данном объекте равно = {self.real_a}'


if __name__ == "__main__":
    my_c = MyClass(-5)
    print(my_c)
