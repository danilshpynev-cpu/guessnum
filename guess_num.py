import random


def guess_number():
    secret = random.randint(1, 100)
    attempts = 0
    while True:
        try:
            guess = int(input('Угадайте число от 1 до 100: '))
        except ValueError:
            print('Введите целое число.')
            continue
        attempts += 1
        if guess < secret:
            print('Больше!')
        elif guess > secret:
            print('Меньше!')
        else:
            print(f'Угадали за {attempts} попыток!')
            break


if __name__ == '__main__':
    guess_number()