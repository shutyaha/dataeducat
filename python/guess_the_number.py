import random



#print(rand_number)

def is_valid(n):
    return (n.isdigit() and 1 <= int(n) <= 100 and n[0] != "0")


def guess_the_number():
    rand_number = random.randint(1, 100)
    print('Добро пожаловать в числовую угадайку')
    while True:
        n = input('Введите число от 1 до 100: ')
        if not is_valid(n):
            print('А может быть все-таки введем целое число от 1 до 100?')
        elif int(n) == rand_number:
            print('Вы угадали, поздравляем!')
            break
        elif int(n) > rand_number:
            print('Ваше число больше загаданного, попробуйте еще разок')
            continue
        elif int(n) < rand_number:
            print('Ваше число меньше загаданного, попробуйте еще разок')
            continue


#n = input('Введите число от 1 до 100: ')
guess_the_number()