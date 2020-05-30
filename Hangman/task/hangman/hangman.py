from random import choice
from string import ascii_lowercase

words_list = ('python', 'java', 'kotlin', 'javascript')
init_word = list(choice(words_list))
init_set = set(init_word)
past_turn_set = set()
answer_word = ['-' for _ in init_word]


def play_hang():
    turn = 8
    while turn != 0:
        print()
        print(*answer_word, sep='')
        turn_char = input('Input a letter: ')
        if turn_char in init_set:
            if turn_char not in answer_word:
                last_index = -1
                for _ in range(init_word.count(turn_char)):
                    answer_word[init_word.index(turn_char, last_index + 1)] = turn_char
                    last_index = init_word.index(turn_char)
            else:
                print('You already typed this letter')
        elif len(turn_char) != 1:
            print('You should input a single letter')
        elif turn_char not in ascii_lowercase:
            print('It is not an ASCII lowercase letter')
        else:
            if turn_char in past_turn_set:
                print('You already typed this letter')
            else:
                print('No such letter in the word')
                turn -= 1
            past_turn_set.add(turn_char)
        if answer_word.count('-') == 0:
            print('You guessed the word ', *answer_word, '!', sep='')
            print('You survived!')
            break
    else:
        print("You are hanged!")


print('H A N G M A N')
action = input('\nType "play" to play the game, "exit" to quit: ')
while True:
    if action == 'play':
        play_hang()
    elif action == 'exit':
        break
    action = input('\nType "play" to play the game, "exit" to quit: ')
