import random


def get_random_decimal():
    my_decimal = random.randint(0, 100)
    return my_decimal


def get_input():
    us_digit = int(input('Введи число: '))
    return us_digit


def get_reaction(right_answer, user_digit):
    if right_answer == user_digit:
        return 'Поздравляю, ты победил!'
    elif right_answer > user_digit:
        return  'Бери больше'
    elif right_answer < user_digit:
        return 'Бери меньше'


def get_lvl():
    print("Select your lvl: easy, medium, high")
    lvl = input()
    if isinstance(lvl, str):
        return lvl
    else:
        raise ValueError("Надо вводить букавы!!!")

def set_health(my_lvl):
    if my_lvl == 'easy':
        health = 50
    elif my_lvl == 'medium':
        health = 25
    elif my_lvl == 'high':
        health = 10
    else:
        raise ValueError("Неверные буковы! Не валидно задал уровни!")
    return health


def main():
    right_answer = get_random_decimal()
    flag = True
    my_lvl = get_lvl()
    my_health = set_health(my_lvl)
    while flag:
        if my_health == 0:
            print('Вы проиграли! :)')
            break
        my_health -= 1
        user_digit = get_input()
        reaction = get_reaction(right_answer, user_digit)
        print(reaction)
        if reaction == 'Поздравляю, ты победил!':
            flag = False
        print(f'Твоё здоровье = {my_health}')

if __name__ == '__main__':
    main()