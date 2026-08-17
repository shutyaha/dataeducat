import random

# Список слов для игры (можно расширить)
words = ['python', 'hangman', 'programming', 'developer', 'algorithm', 'function', 'variable']

def get_word():
    return random.choice(words).upper()

def display_word(word, guessed_letters):
    return ' '.join([ch if ch in guessed_letters else '_' for ch in word])

def draw_hangman(mistakes):
    stages = [
        '''
           ------
           |    |
           |
           |
           |
           |
        --------
        ''',
        '''
           ------
           |    |
           |    O
           |
           |
           |
        --------
        ''',
        '''
           ------
           |    |
           |    O
           |    |
           |
           |
        --------
        ''',
        '''
           ------
           |    |
           |    O
           |   /|
           |
           |
        --------
        ''',
        '''
           ------
           |    |
           |    O
           |   /|\\
           |
           |
        --------
        ''',
        '''
           ------
           |    |
           |    O
           |   /|\\
           |   /
           |
        --------
        ''',
        '''
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |
        --------
        '''
    ]
    print(stages[mistakes])

def play_hangman():
    word = get_word()
    guessed_letters = set()
    mistakes = 0
    max_mistakes = 6

    print('Добро пожаловать в игру "Угадайка слов" (Hangman)!')
    print('Угадай слово, пока виселица не построена полностью.')

    while mistakes < max_mistakes:
        print('\n' + display_word(word, guessed_letters))
        draw_hangman(mistakes)

        if all(ch in guessed_letters for ch in word):
            print(f'\nПоздравляю! Ты угадал слово: {word}')
            break

        guess = input('\nВведи букву: ').strip().upper()

        if len(guess) != 1 or not guess.isalpha():
            print('Пожалуйста, введи одну букву.')
            continue

        if guess in guessed_letters:
            print('Ты уже называл эту букву.')
            continue

        guessed_letters.add(guess)

        if guess not in word:
            mistakes += 1
            print(f'Неверно! Осталось попыток: {max_mistakes - mistakes}')
        else:
            print('Верно!')

    else:
        draw_hangman(mistakes)
        print(f'\nИгра окончена. Ты проиграл.')
        print(f'Загаданное слово было: {word}')

# Запуск игры
play_hangman()