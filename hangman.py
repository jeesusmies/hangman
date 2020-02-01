import json
import os
import sys
import random
import string

chars = string.ascii_letters

# please forgive me for my crappy english and comments. I'm trying to improve them.

print("Welcome to Ilhu's hangman game!\nType 1 to countinue.\n")

# Turns strings into lists, so that the characters in strings can be changed.
def turn_string_into_list(string):
    result = []
    for char in string:
        result.append(str(char))
    return result

# Does the opposite that the turn_string_into_list() does. This is used for the .find().
def turn_list_into_string(list):
    result = ''
    for element in list:
        result += str(element)
    return result

# Loops this loop until the user has inputted a number. The same loop can be seen in my "password-generator".
while True:
    try:
        inputGameMode = int(input(">> "))
    # If a ValueError happens, it requests the user to input the again until a number has been inputted.
    except ValueError:
        print("Please input a number.")
    # If something else than a ValueError happens, the game shuts down.
    except:
        print("Something went wrong, exitting.")
        sys.exit(0)
    # If no errors happen, continue.
    else:
        break

# Here begins the game. too lazy to do here comments for now.
if inputGameMode == 1:
    with open('words.json', 'r') as wordsFile:
        words = json.load(wordsFile)
        hangmanWord = turn_string_into_list(random.choice(words))
        wordHidden = turn_string_into_list(''.join('_' for i in range(len(hangmanWord))))
        wrongAnswerAmount = 0
        rightAnswerAmount = 0

        print(f"Here is your word. It has {len(hangmanWord)} letters.\n{''.join(wordHidden)}")
        print("Guess a letter.\n")

        while True:
            if wrongAnswerAmount >= 8 or rightAnswerAmount == len(turn_list_into_string(hangmanWord)):
                break
            inputLetter = str(input(">> "))
            result = turn_list_into_string(hangmanWord).find(inputLetter)
            if result != -1:
                rightAnswerAmount += 1
                for i in range(hangmanWord.count(inputLetter)):
                    result = turn_list_into_string(hangmanWord).find(inputLetter)
                    wordHidden[result], hangmanWord[result] = hangmanWord[result], wordHidden[result]
                print(f"Nice, you found a letter.\n{''.join(wordHidden)}")
            else:
                wrongAnswerAmount += 1
                print(f"Letter not found. Wrong answers: {wrongAnswerAmount}")

        if wrongAnswerAmount >= 8:
            print(f"You lost.\nYou guessed {wrongAnswerAmount+rightAnswerAmount} times!")
        else:
            print(f"Wow! You won!\nYou guessed {wrongAnswerAmount+rightAnswerAmount} times!")
