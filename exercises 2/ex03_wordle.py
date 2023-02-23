"""EX03 - Structured Wordle!"""

__author__ = "730556876"

def contains_char(guess_word, single_letter) -> bool:
    """Searches each word for the guessed lettter"""
    assert len(single_letter) == 1
    guess_idx: int = 0
    while guess_idx < len(guess_word):
        if single_letter == guess_word[guess_idx]:
            return True
        guess_idx = guess_idx + 1
    return False

def emojified (guess_word, secret_word) -> str:
    """Returns a color coded score for each letter"""
    assert len(guess_word) == len(secret_word)
   
    green_box: str = "\U0001F7E9"
    white_box: str = "\U00002B1C"
    yellow_box: str = "\U0001F7E8"
    result_string: str = ""

    guess_idx: int = 0
    while guess_idx < len(guess_word):
        result = contains_char(secret_word,guess_word[guess_idx])
        if result == True:
            if secret_word[guess_idx] == guess_word[guess_idx]:
                result_string += green_box
            else:
                result_string += yellow_box
        else:
            result_string += white_box
        guess_idx = guess_idx + 1
    return result_string

def input_guess(expected_length) -> str:
    guess_word: str = input("Enter a " + str(expected_length) + " character word:")
    while len(guess_word) != expected_length:
        guess_word = input("That wasn't " + str(expected_length) + " chars! Try again:")
    return guess_word

def main() -> None:
    """The entrypoint of the program and main game loop."""
    
    secret_word: str = "codes"
    turn_number: int = 1

    while turn_number <= 6:
        print("=== Turn " + str(turn_number) + "/6 ===")
        guess_word = input_guess(len(secret_word))
        print(emojified(guess_word,secret_word))
        if guess_word == secret_word:
            print("You won in " + str(turn_number) + "/6 turns!")
            return
        turn_number = turn_number + 1
    print("X/6 - Sorry, try again tomorrow!")

if __name__ == "__main__":
    main()