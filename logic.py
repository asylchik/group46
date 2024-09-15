import random


def play_game(min_value, max_value, attempts, initial_capital):
    secret_number = random.randint(min_value, max_value)
    capital = initial_capital
    for attempt in range(1, attempts+1):
        print(f'\nПопытка {attempt} из {attempts}')
        print(f'Ваш текущий капиатал: {capital}')
        try:
            bet = int(input('Введите вашу ставку: '))
        except:
            print('Введите корректное число!')
            continue
        if bet > capital:
            print('У вас недостаточно денег для ставки')
            continue
        try:
            gues = int(input(f'Угадайте число от {min_value} до {max_value} '))
        except:
            print('Ввведите корректное число')
            continue
        if gues < min_value or gues > max_value:
            print(f'Число должно быть в диапазоне от {min_value} до {max_value}')
            continue
        if gues == secret_number:
            print(f'Поздравляем! Вы угадали число {secret_number}')
            print(f'Ваш выигрыш {bet * 2}')
            print(f'Капитал {capital}')
            break
        else:
            print(f'Неверно загаданное число {secret_number}')
            capital -= bet
        if capital <= 0:
            print('У вас закончились деньги')
            break
    else:
        print(f'\n Игра окончено! Загаданное число было {secret_number}.Ваш капитал {capital}')