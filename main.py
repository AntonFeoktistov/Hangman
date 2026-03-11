import random
from pictures import get_picture

ALPHABET= "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзхийклмнопрстуфхцчшщъыьэюя"

def init_dictionary():
     with open("words.txt", 'r', encoding='utf-8') as file:
        text = file.read()
        words = text.split()
        return words   
        




def get_char_from_user():
    char = input("Введите букву русского алфавита ")  
    if len(char) == 1 and char in ALPHABET:
        return char.lower()
    else:
        while True:
            char = input("Неверный ввод! Введите русскую букву ")
            if len(char) ==1 and char in ALPHABET:
                return char.lower()

def is_game_over(word_mask, mistakes):
    if ('*' not in word_mask or mistakes == 0):
        return True
    return False

def open_chars(WORD, word_mask, char):
    for i in range(len(WORD)):
        if char==WORD[i]:
            word_mask[i] = WORD[i] 

def say_is_char_in_mask(WORD, word_mask, char):
    if char in word_mask:
        print("Есть такая буква!")
    else:
        print("Нет такой буквы!")

def show_start_menu():
    print("Чтобы начать игру, нажмите любую букву, чтобы выйти, нажмите в ")
    inp = input()
    if inp =="в":
        print("Программа завершена")
        exit()


def start_game(words: list):
    show_start_menu()
    
    WORD = random.choice(words) 
    word_mask = list(len(WORD) * '*')
    chars_history = set() 
    mistakes = 7

    while(not is_game_over(word_mask, mistakes)):
        print(f"У вас есть {mistakes} попыток чтобы отгадать слово {''.join(word_mask)}")
        char = get_char_from_user() 
        if char in chars_history:
                print("Вы уже вводили такую букву. Введите другую")
        elif char not in chars_history:
            chars_history.add(char) 
            if char not in WORD: 
                mistakes-=1
            open_chars(WORD, word_mask, char)
            say_is_char_in_mask(WORD, word_mask, char)
        print(get_picture(mistakes))

    if mistakes==0:
        print(f"Вы проиграли! Было загадано слово {WORD}") 
    if mistakes>0:
        print(f"Вы выиграли! Было загадано слово {WORD}")

if __name__ == "__main__":
    words = init_dictionary()
    while True:
        start_game(words)
    


