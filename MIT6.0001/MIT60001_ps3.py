# Problem Set 3, word game

import re
import math
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10, '*': 0
}

# -----------------------------------
# Helper code

WORDLIST_FILENAME = "MIT60001_ps3.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	
#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.
    """
    wordlen = len(word)
 
    if wordlen == 0: return 0
    word = word.lower()
    total_score = 0
 
    for letter in word:
        total_score += SCRABBLE_LETTER_VALUES[letter]
    total_score *= max(1, (7*wordlen) - (3*(n-wordlen)))
    return total_score

#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    
    for letter in hand.keys():
        print((letter + ' ') * hand[letter], end=' ')
    print()

#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    
    hand={}
    num_vowels = int(math.ceil(n / 3))

    for i in range(num_vowels - 1):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
    
    # Generate wildcard
    hand["*"] = 1

    for i in range(num_vowels, n):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    
    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    ret = hand.copy()
    for letter in word.lower():
        ret[letter] = max(0, ret.get(letter, 0) - 1)

    return ret

#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
   
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """
    word = word.lower()
    match = False
    for dict_word in word_list:
        # see if possible match
        reg = "^" + word.replace("*", "[aeiou]") + "$"
        if re.findall(reg, dict_word):
            match = True
            break
    if not match: return False

    word_freq_dict = get_frequency_dict(word)
    for letter in word_freq_dict:
        if hand.get(letter, 0) < word_freq_dict.get(letter, 0):
            return False
    return True

#
# Problem #5: Playing a hand
#
def calculate_handlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    # print(hand)
    length = 0
    for letter in hand:
        length += hand[letter]
    return length

def play_hand(hand, word_list):

    """
    Allows the user to play the given hand, as follows:

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand
      
    """
    total_score = 0

    while calculate_handlen(hand) != 0:
        print("Your hand:", end=" ")
        display_hand(hand)
        user_input = input("Enter !! to quit, or enter a word.\n")
        
        if user_input == "!!":
            break
        
        if is_valid_word(user_input, hand, word_list):
            word_score = get_word_score(user_input, calculate_handlen(hand))
            print("Correct word! Score is", word_score)
            total_score += word_score
        else:
            print("Incorrect word")
        hand = update_hand(hand, user_input)                    
    return total_score

#
# Problem #6: Playing a game
# 

def substitute_hand(hand, letter):
    """ 
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """
    ret_hand = hand.copy()
    if ret_hand.get(letter, None) is None: return ret_hand

    new_letter = None
    while True:
        new_letter = random.choice(CONSONANTS + VOWELS)
        if not new_letter in ret_hand: break
    ret_hand[new_letter] = ret_hand[letter]
    del(ret_hand[letter])
    return ret_hand
       
def play_game(word_list):
    """
    Allow the user to play a series of hands
    word_list: list of lowercase strings
    """
    while True:
        try:
            rounds = int(input("How many rounds do you want to play?  "))
            break
        except:
            print("Enter a number please")

    cumulative_score = 0
    substituted = False
    replayed = False

    for i in range(rounds):
        print("\n\nStarting round", i + 1)
        hand = deal_hand(HAND_SIZE)
        display_hand(hand)
        if substituted == False and input("Would you like to substitute a letter?").lower() == "yes":
            letter = input("What letter would you like to switch?")
            hand = substitute_hand(hand, letter)
            substituted = True

        # Play the hand
        hand_score = play_hand(hand, word_list)
        if replayed == False and input("Would you like to replay this hand?").lower() == "yes":
            hand_score = max(hand_score, play_hand(hand , word_list))
        cumulative_score += hand_score
        print("Round over.\tTotal score thus far is", cumulative_score)
    
    print("Overall score:::::", cumulative_score)
    return cumulative_score

#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
