import random


digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'

chars = ''

# Считывание пользовательских данных
password_count = int(input('Введите количество паролей для генерации: '))
password_length = int(input('Введите длину одного пароля: '))

use_digits = input('Включать ли цифры (0123456789)? (д/н): ').strip().lower() == 'д'
use_uppercase = input('Включать ли прописные буквы (ABCDEFGHIJKLMNOPQRSTUVWXYZ)? (д/н): ').strip().lower() == 'д'
use_lowercase = input('Включать ли строчные буквы (abcdefghijklmnopqrstuvwxyz)? (д/н): ').strip().lower() == 'д'
use_punctuation = input('Включать ли символы (!#$%&*+-=?@^_)? (д/н): ').strip().lower() == 'д'
exclude_ambiguous = input('Исключать ли неоднозначные символы (il1Lo0O)? (д/н): ').strip().lower() == 'д'


# Формирование chars
if use_digits:
    chars += digits
if use_uppercase:
    chars += uppercase_letters
if use_lowercase:
    chars += lowercase_letters
if use_punctuation:
    chars += punctuation

# Исключение неоднозначных символов
if exclude_ambiguous:
    ambiguous = 'il1Lo0O'
    for ch in ambiguous:
        chars = chars.replace(ch, '')


def generate_password(length, alphabet):
    password = ''
    for _ in range(length):
        password += random.choice(alphabet)
    return password


# Генерация паролей
for i in range(password_count):
    print(f'Пароль {i + 1}: {generate_password(password_length, chars)}')


