# Problem Set 2, hangman.py

# Hangman Game
# -----------------------------------
# Helper code
import random
import string

WORDLIST_FILENAME = "MIT60001-ps2.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    return all(letter in letters_guessed for letter in secret_word)

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    return ''.join([letter if letter in letters_guessed else "_ " for letter in secret_word])

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    return ''.join([letter for letter in string.ascii_lowercase if letter not in letters_guessed])

def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    my_word = my_word.replace(" ", "")
    if len(my_word) != len(other_word): return False
    # Build dict of word
    other_word_dist = {}
    for (i, letter) in enumerate(other_word):
      if not letter in other_word_dist:
        other_word_dist[letter] = []
      other_word_dist[letter].append(i)

    # Match my_word with dict above
    for letter in other_word_dist:
      my_word_distribution = set(my_word[pos] for pos in other_word_dist[letter])
      if len(my_word_distribution) != 1 or (not letter in my_word_distribution and not "_" in my_word_distribution):
        return False
    return True

def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    matches = []
    for word in wordlist:
      if match_with_gaps(my_word, word): matches.append(word)
    if len(matches) != 0:
      for word in matches: print(word, end=" ")
      print("\n")
    else:
      print("No matches found")



def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    Starts up an interactive game of Hangman.
    '''

    guesses = 6
    warnings = 3
    letters_guessed = []
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secret_word), "letters long.")

    while guesses > 0:
      print("You have", guesses, "guesses left, and", warnings, "warnings left.")
      print("Available letters", get_available_letters(letters_guessed))

      while True:
        try:
          letter = input("Enter a new letter: ").lower()
          if letter != "*" and (not letter.isalpha() or len(str(letter)) != 1 or letter in letters_guessed):
            raise ValueError
          break
        except:
          print("You must enter a single, previously unpicked letter, or *!")
          if warnings > 0:
            warnings -= 1
            print("You lose a warning; you have", warnings, "warnings left.")
          elif warnings == 0:
            print("You can't pick a letter? You lose a guess! You have", guesses, "guesses.")
            guesses -= 1
      
      # Update guesses, show user if not *
      if letter != "*": letters_guessed.append(letter)

      # Check for win
      if is_word_guessed(secret_word, letters_guessed):
        print ("You win! Score was", guesses * len(set(secret_word)))
        return True

      # Check for hint
      if letter == "*":
        print("Here are the possible matches!")
        show_possible_matches(get_guessed_word(secret_word, letters_guessed))
        continue

      if letter in secret_word:
        print("Good guess! The letter", letter, "is in the word.")
      else:
        print("The letter", letter, "is not in the word. Try again.")
        if letter in ['a', 'e', 'i', 'o', 'u']:
          guesses -= 2
        else:
          guesses -= 1
      print(get_guessed_word(secret_word, letters_guessed))
      print("-----------------------")

    return False

# -----------------------------------




def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    Starts up an interactive game of Hangman.
    
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass


word = choose_word(wordlist)
if not hangman(word):
  print ("You lose, the word was", word)
