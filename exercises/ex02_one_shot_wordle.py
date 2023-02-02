"""EX02 - One Shot Wordle - Loops"""

__author__= "730556876"

secret_word: str = "knoll"
guess: str = input ("What is your " + str(len(secret_word)) + "-letter guess? ")

g_idx: int = 0
s_idx: int = 0
letter = False
green_box: str = "\U0001F7E9"
white_box: str = "\U00002B1C"
yellow_box: str = "\U0001F7E8"

while len(guess) != len(secret_word):
    guess: str = input ("That was not " + str(len(secret_word)) + " letters! Try again: ")

result_string: str = ""

while g_idx < len(guess):
    if guess[g_idx] == secret_word[g_idx]:
        result_string += green_box
    else:
        letter = False
        s_idx = 0
        while s_idx < len(secret_word):
            if guess[g_idx] == secret_word[s_idx]:
                letter = True
            s_idx = s_idx + 1
        if letter == True:
            result_string += yellow_box
        else:
            result_string += white_box
    g_idx = g_idx + 1

print(result_string)

if guess == secret_word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")