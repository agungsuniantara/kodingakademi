"""CSC108: Fall 2024 -- Assignment 0: Word Voyager

This code is provided solely for the personal and private use of students taking
CSC108 at the University of Toronto Mississauga. Copying for purposes other than this use is
expressly prohibited. All forms of distribution of this code, whether as given
or with any changes, are expressly prohibited.

All of the files in this directory and all subdirectories are:
Copyright (c) 2024 Rutwa Engineer, Dan Zingaro, Peter Dixon, Randy Hickey, Romina Piunno
"""

"""The script that runs the game of word voyager."""

# Add any necessary imports up here

from settings import WORD, MAX_NUM_ERRORS
from wordvoyager import obfuscated_word, get_guess, format_guesses, is_guess_good, is_word_guessed

def main() -> bool:
    """The main code for this script. Runs the word voyager game."""
    # Write your code as detailed in the assignment handout here

    past_guesses = []
    incorrect_guesses = 0

    while incorrect_guesses < MAX_NUM_ERRORS:

        print(f"Word: {obfuscated_word(WORD, past_guesses)}")
        print(f"Number of bad guesses: {incorrect_guesses} out of {MAX_NUM_ERRORS}")
        print(f"Guesses: {format_guesses(past_guesses)}")

        guess = get_guess(past_guesses)

        if is_guess_good(WORD, guess):
            print(f"Good guess! The letter '{guess}' is in the word.")
        else:
            print(f"Bad guess! The letter '{guess}' is not in the word.")
            incorrect_guesses += 1

        if is_word_guessed(WORD, past_guesses):
            print(f"Congratulations! You guessed the word: {WORD}")
            return True

    print(f"Sorry, you've run out of guesses. The word was: {WORD}")
    return False

if __name__ == '__main__':
    # import python_ta
    #
    # python_ta.check_all(config={
    #     "allowed-io": ["main"],
    #     "allowed-import-modules": [
    #         "settings",
    #         "python_ta",
    #         "wordvoyager",
    #     ],
    # })
    main()  # Don't modify this part!
