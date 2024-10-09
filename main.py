import time
from random import choice

print('Виселица')
time.sleep(1)
print('Тема: игры')
time.sleep(1)
def choose_word():
    words = ['brawlstars','pubgmobile','standoff2','roblox','callofduty','zelda']
    return choice(words)
def display_hangman(tries):
    stages = [
        """
           --------
           |      |
           |      O
           |     /|\\
           |     / \\
           |
        """,
        """
           --------
           |      |
           |      O
           |     /|\\
           |     / 
           |
        """,
        """
           --------
           |      |
           |      O
           |     /|\\
           |      
           |
        """,
        """
           --------
           |      |
           |      O
           |     /|
           |      
           |
        """,
        """
           --------
           |      |
           |      O
           |      |
           |     
           |
        """,
        """
           --------
           |      |
           |      O
           |      
           |     
           |
        """,
        """
           --------
           |      |
           |      
           |      
           |     
           |
        """,
        """
           --------
           |      
           |      
           |      
           |     
           |
        """
    ]
    return stages[tries]
def play():
    display = 7
    stop = 0
    allletter = []
    word = choose_word()
    sticks=['_']*len(word)
    print(display_hangman(7),*sticks)
    while stop == 0:
        control = 0
        time.sleep(1)
        print('Впишите букву:')
        time.sleep(1)
        letter = input().lower()
        if letter in allletter:
            pass
        else:
            allletter.append(letter)
        time.sleep(0.7)
        if len(letter) == 1:
            for i in range(len(word)):
                if word[i] == letter:
                    del sticks[i]
                    sticks.insert(i,letter)
                    control = 1
                if i == len(word)-1 and control == 0:
                    display -= 1
            time.sleep(0.5)
            if control == 1:
                print('Правильно')
            else:
                print('Неправильно')
            time.sleep(0.5)
            print(display_hangman(display),*sticks)
            time.sleep(1)
            print('Использованные буквы:',*allletter)
            time.sleep(1)
            if display == 0:
                stop = 1
            if ''.join(sticks) == word:
                stop = 2
    if stop == 1:
        print('Вы проиграли')
        time.sleep(1)
        print('Слово было:', word)
    else:
        print('Вы победили')
play()