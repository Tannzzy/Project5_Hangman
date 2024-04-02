import random
from hangman_word_and_stage import word_list, stage

# print opening title screen
print('''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    
''')
print("welcome to my hangman game, lets play!\n")

# chose random word from world_list
chosen_word = random.choice(word_list)

# initiate number of underscore needed to be displayed
hud = []
word_length = len(chosen_word)
for letter in range(0, word_length + 1):
    if len(hud) != letter:
        hud.extend("_")

# initiate stage displayed and list of letters guessed
lives = 6
stage_digit = 0
guess_list = []

# game
while "_" in hud and lives > 0:
    guess = input("guess a letter: ").lower()

    if guess not in chosen_word and guess not in guess_list:
        lives -= 1
        stage_digit += 1
        print(stage[stage_digit])
        print(f"You guessed {guess}, that's not in the word. You have {lives} lives left")
    else:
        print(stage[stage_digit])

    for pos in range(word_length):
        if chosen_word[pos] == guess:
            hud[pos] = guess
    print(f"{' '.join(hud)}\n\n")

    if guess in guess_list:
        print(f"you've already guessed the letter {guess}, try again")
    else:
        guess_list.extend(guess)

if lives == 0:
    print("game over :(")

if "_" not in hud:
    print("you win :)")