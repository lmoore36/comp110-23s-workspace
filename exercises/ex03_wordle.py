"""EX03 - Structured Wordle!"""

__author__ = "730556876"
guess_word: str = input("Enter a 5 character word:")
single_letter: str = input("Guess a letter:")
guess_idx: int = 0


def contains_char(guess_word, single_letter):
    """Searches each word for the guessed lettter"""
    while guess_idx < len(guess_word):
        if single_letter == guess_word[guess_idx]:
            return True
        guess_idx = guess_idx + 1
        return False
    


           
