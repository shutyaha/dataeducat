# Алфавиты
ru_lower = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
ru_upper = ru_lower.upper()
en_lower = 'abcdefghijklmnopqrstuvwxyz'
en_upper = en_lower.upper()


def caesar_cipher(text, direction, lang, shift):
    # direction: 'encrypt' или 'decrypt'
    # lang: 'ru' или 'en'
    # shift: шаг сдвига (вправо для шифрования)

    if direction == 'decrypt':
        shift = -shift

    result = ''

    if lang == 'ru':
        lower_alphabet = ru_lower
        upper_alphabet = ru_upper
        alphabet_size = 32
    else:  # 'en'
        lower_alphabet = en_lower
        upper_alphabet = en_upper
        alphabet_size = 26

    for ch in text:
        if ch in lower_alphabet:
            idx = lower_alphabet.index(ch)
            new_idx = (idx + shift) % alphabet_size
            result += lower_alphabet[new_idx]
        elif ch in upper_alphabet:
            idx = upper_alphabet.index(ch)
            new_idx = (idx + shift) % alphabet_size
            result += upper_alphabet[new_idx]
        else:
            # Неалфавитные символы не меняются
            result += ch

    return result


# Ввод данных от пользователя
direction = input('Выберите направление (шифрование/дешифрование): ').strip().lower()
while direction not in ['шифрование', 'дешифрование']:
    direction = input('Введите "шифрование" или "дешифрование": ').strip().lower()

lang = input('Выберите язык алфавита (русский/английский): ').strip().lower()
while lang not in ['русский', 'английский']:
    lang = input('Введите "русский" или "английский": ').strip().lower()

shift = int(input('Введите шаг сдвига (целое число): '))

text = input('Введите текст: ')

# Приведение направления и языка к внутреннему формату
dir_code = 'encrypt' if direction == 'шифрование' else 'decrypt'
lang_code = 'ru' if lang == 'русский' else 'en'

# Шифрование / дешифрование
result_text = caesar_cipher(text, dir_code, lang_code, shift)
print('\nРезультат:')
print(result_text)