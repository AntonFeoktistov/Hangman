import random
import pictures 
alf= "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзхийклмнопрстуфхцчшщъыьэюя"
def init_dictionary():
     with open("words.txt", 'r', encoding='utf-8') as file:
        text = file.read()
        words = text.split()
        return words      
words = init_dictionary() 
def choose_hard(hard_level):
    match hard_level:
        case "н":
            return 11
        case "р":
            return 8
        case _:
            return 5
def get_char():
    
    ch = input("Введите букву русского алфавита ")  
    if len(ch) == 1 and ch in alf:
        return ch
    else:
        while True:
            ch = input("Неверный ввод! Введите русскую букву ")
            if ch in alf:
                return ch

def is_game_over(WORD, word, mistakes):
    if ('*' not in word) or mistakes == 0:
        return True
    return False
def open_chars(WORD, word, ch):
    for i in range(len(WORD)):
        if ch==WORD[i]:
            word[i] = WORD[i] 
    return word


def start_game():
    inp = input("Чтобы нажать игру, нажмите любую букву, чтобы выйти, нажмите в ")
    if inp=="в":
        exit() 
    print("Выберите уровень сложности")
    hard_level = input("Низкий (11 попыток): нажмите н, средний(8) - р, высокий(5) - любая другая буква")
    mistakes = choose_hard(hard_level) 
    pict = 0 
    WORD = random.choice(words) 
    word = list(len(WORD) * '*')
    chars_history = set() 
    while(not is_game_over(WORD, word, mistakes)):
        print(f"У вас есть {mistakes} попыток чтобы отгадать слово {''.join(word)}")
        ch = get_char() 
        if ch not in chars_history and ch in alf:
            chars_history.add(ch) 
            pict+=1
            mistakes-=1
        word = open_chars(WORD, word, ch) 
        print(pictures.pictures[pict])
    if mistakes==0:
        print(f"Вы проиграли! Было загадано слово {WORD}") 
    if mistakes>0:
        print(f"Вы выйграли! Было загадано слово {WORD}")

while True:
    start_game()

