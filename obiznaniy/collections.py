class Triangle:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return f'Сторона а = {self.a}, сторона b = {self.b}, сторона c = {self.c}'

    def __repr__(self):
        return f'Сторона а = {self.a}, сторона b = {self.b}, сторона c = {self.c}'

    def __setattr__(self, key, value):
        super.__setattr__(self, key, value)
        print('ЖОПА!')


if __name__ == "__main__":
    my_triangle = Triangle(a = 7,
                           b = 8,
                           c = 9)

    list_of_triangles = list()
    list_of_triangles.append(my_triangle)
    print(my_triangle)
    my_triangle.a = 5*(10**5)
    print(my_triangle)