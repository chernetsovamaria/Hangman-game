def user_input():
    return input('Введите букву: ').lower()


def welcome_speech(t, lives):
    print(f'''Добро пожаловать в игру hangman!
Ваш задача - угадать слово за несколько попыток,
иначе вас ждёт расплата!
Загаданное слово состоит из {len(t)} букв: {t}
Вам даётся попыток: {lives}''')


def list_to_string_convert(c):
    s = ''
    return s.join(c)


def start_template(w):
    return '_' * len(w)


def get_word(w):
    return w[0]


def build_template(t, w, g):
    l_template = list(t)
    if g in w:
        l_template[w.index(g)] = g
    else:
        l_template = t
    return l_template


def game():
    progress = True
    word = ['orange']
    lives = 3
    word_in_play = get_word(word)  # исп. слово
    template = start_template(word_in_play)  # строка из '_' длины исп. слова
    for_comparison = template
    welcome_speech(list_to_string_convert(template), lives)  # выводит приветствие
    while progress:
        user_guess = user_input()
        template = build_template(template, word_in_play, user_guess)
        print(f'Результат: {list_to_string_convert(template)}')
        if for_comparison == template:
            if lives == 1:
                print('Вы проиграли')
                progress = False
            else:
                print(f'У вас осталось попыток: {lives - 1}')
                lives -= 1
        for_comparison = template
        if list_to_string_convert(template) == word_in_play:
            print('Вы выиграли!')
            progress = False


game()
