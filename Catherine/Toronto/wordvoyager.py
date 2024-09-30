"""CSC108: Fall 2024 -- Assignment 0: Word Voyager

This code is provided solely for the personal and private use of students taking
CSC108 at the University of Toronto Mississauga. Copying for purposes other than this use is
expressly prohibited. All forms of distribution of this code, whether as given 
or with any changes, are expressly prohibited.

All of the files in this directory and all subdirectories are:
Copyright (c) 2024 Rutwa Engineer, Dan Zingaro, Peter Dixon, Randy Hickey, Romina Piunno
"""

"""Some functions useful for the wordvoyager game.
Starter code
"""

import doctest


def obfuscated_word(word, past_guesses):
    """

    :param word:
    :param past_guesses:
    :return:

    >>> obfuscated_word('headphones', ['e', 'd'])
    '_ e _ d _ _ _ _ e _'
    """
    data = []
    for letter in word:
        if letter in past_guesses:
            data.append(letter)
        else:
            data.append("_")

    return " ".join(data)


def get_guess(past_guesses):
    while True:
        guess = input("Guess a letter: ")

        if len(guess) != 1:
            print("Please enter only one letter.")

        elif not guess.isalpha():
            print("Please enter a valid alphabetical letter.")

        elif guess in past_guesses:
            print("You have already guessed that letter. Try again.")

        else:
            past_guesses.append(guess)
            return guess

def format_guesses(past_guesses):
    """

    :param past_guesses:
    :return:

    >>> format_guesses(['a', 'b', 'c'])
    'a b c'
    """
    result = []
    for guess in past_guesses:
        result.append(guess)

    return " ".join(result)

def is_guess_good(word, guess):
    """

    :param word:
    :param guess:
    :return:
    >>> is_guess_good('toe', 'e')
    True
    >>> is_guess_good('toe', 'a')
    False
    """
    if guess in word:
        return True
    else:
        return False

def is_word_guessed(word, past_guesses):
    """

    :param word:
    :param past_guesses:
    :return:
    >>> is_word_guessed('toe', ['t', 'o', 'e'])
    True
    >>> is_word_guessed('toe', ['t', 'a'])
    False
    """
    for letter in word:
        if letter not in past_guesses:
            return False
    return True

if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        "allowed-io": ["get_guess"],
        "allowed-import-modules": [
            "python_ta",
        ],
    })
    # If you'd like to write testing code for this assignment, you may do so
    # here. You may also include doctests if you feel they will give you better
    # testing.
