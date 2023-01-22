"""EX01 Program - Wordle."""

__author__ = "730556876"

word_guess: str = input("Enter a 5-character word:")

if len(word_guess) != 5:
    print("Error: Word must contain 5 characters")
    exit()

letter: str = input("Enter a single character:")

if len(letter) != 1:
    print("Error: Character must be a single character.")
    exit()

total_count: int = word_guess.count(letter)

print("Searching for " + letter + " in " + word_guess)

if (letter == word_guess[0]):
    print(letter + " found at index 0")

if (letter == word_guess[1]):
    print(letter + " found at index 1")

if (letter == word_guess[2]):
    print(letter + " found at index 2")

if (letter == word_guess[3]):
    print(letter + " found at index 3")

if (letter == word_guess[4]):
    print(letter + " found at index 4")

if (total_count == 1):
    print(str(total_count) + " instance of " + letter + " found in " + word_guess)
elif (total_count == 0):
    print("No instances of " + letter + " found in " + word_guess)
else:
    print(str(total_count) + " instances of " + letter + " found in " + word_guess)