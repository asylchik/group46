from logic import play_game
from decouple import config


def load_settings():
    min_value = config('min_value', default=1, cast=int)
    max_value = config('max_value', default=100, cast=int)
    attempts = config('attempts', default=5, cast=int)
    initial_capital = config('initial_capital', default=1000, cast=int)

    return min_value, max_value, attempts, initial_capital


def main():
    min_value, max_value, attempts, initial_capital = load_settings()
    play_game(min_value, max_value, attempts, initial_capital)


if __name__ == '__main__':
    main()
