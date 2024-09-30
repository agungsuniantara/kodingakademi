"""CSC108: Fall 2024 -- Assignment 0: Word Voyager

This code is provided solely for the personal and private use of students taking
CSC108 at the University of Toronto Mississauga. Copying for purposes other than this use is
expressly prohibited. All forms of distribution of this code, whether as given 
or with any changes, are expressly prohibited.

All of the files in this directory and all subdirectories are:
Copyright (c) 2024 Rutwa Engineer, Dan Zingaro, Peter Dixon, Randy Hickey, Romina Piunno
"""
"""Settings for the word voyager game."""

# Modify these settings at your will in order to test your game

# WORD is the word in question we'll be using for our game of wordvoyager
WORD = 'tetrachlorodibenzoparadioxin'
# Feel free to have enter a random word above without looking, so that you
# can play the game yourself without knowing the word in advance.

# If the user makes more than MAX_NUM_ERRORS number of incorrect guesses, they
# lose the game.
MAX_NUM_ERRORS = 5

# Don't touch these assertions!
assert WORD.isalpha()  # Make sure WORD is alphabetic-only and lower case
assert WORD.islower()
assert MAX_NUM_ERRORS >= 1  # Make sure MAX_NUM_ERRORS is positive
