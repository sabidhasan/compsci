# Problem Set 4C

import string
from MIT60001_ps4a import get_permutations

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

WORDLIST_FILENAME = 'MIT60001_ps4_words.txt'

# you may find these constants helpful
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'

class SubMessage(object):
    def __init__(self, text):
        '''
        Initializes a SubMessage object
        text (string): the message's text
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)
    
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        '''
        return self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        '''
        return self.valid_words
                
    def build_transpose_dict(self, vp):
        '''
        vowels_permutation (string): a string containing a permutation of vowels (a, e, i, o, u)

        Example: When input "eaiuo":
        Mapping is a->e, e->a, i->i, o->u, u->o
        and "Hello World!" maps to "Hallu Wurld!"

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        ret = {}
        for letter in string.ascii_uppercase + string.ascii_lowercase:
            ret[letter] = letter
        for i, letter in enumerate(VOWELS_LOWER):
            ret[letter] = vp[i]
        for i, letter in enumerate(VOWELS_UPPER):
            ret[letter] = vp[i].upper()
        return ret
    
    def apply_transpose(self, transpose_dict):
        '''
        transpose_dict (dict): a transpose dictionary
        
        Returns: an encrypted version of the message text, based 
        on the dictionary
        '''
        letters = list(self.get_message_text())
        for i, letter in enumerate(letters):
            letters[i] = transpose_dict.get(letter, letter)
        return ''.join(letters)
        
class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
        '''
        Initializes an EncryptedSubMessage object
        text (string): the encrypted message text
        '''
        super().__init__(text)

    def decrypt_message(self):
        '''
        Attempt to decrypt the encrypted message 
        
        Idea is to go through each permutation of the vowels and test it
        on the encrypted message. For each permutation, check how many
        words in the decrypted text are valid English words, and return
        the decrypted message with the most English words.
        
        If no good permutations are found (i.e. no permutations result in 
        at least 1 valid word), return the original string. If there are
        multiple permutations that yield the maximum number of words, return any
        one of them.

        Returns: the best decrypted message    
        
        Hint: use your function from Part 4A
        '''
        # Get all permutations of vowels
        max_match_count = 0
        max_match_permutation = ""
        for vowel_possiblility in get_permutations(VOWELS_LOWER):
            # Try with current vowels
            curr_sentence = self.apply_transpose(self.build_transpose_dict(vowel_possiblility))
            # Count number of matches
            curr_match_count = 0
            for curr_word in curr_sentence.split(" "):
                if is_word(self.valid_words, curr_word):
                    curr_match_count += 1
            if curr_match_count > max_match_count:
                max_match_count = curr_match_count
                max_match_permutation = vowel_possiblility
        if max_match_count == 0: 
            return self.get_message_text()
        return self.apply_transpose(self.build_transpose_dict(max_match_permutation))
    
if __name__ == '__main__':
    # Example test case
    message = SubMessage("Hello World!")
    permutation = "eaiuo"
    enc_dict = message.build_transpose_dict(permutation)
    assert message.apply_transpose(enc_dict) == "Hallu Wurld!"

    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    assert enc_message.decrypt_message() == 'Hello World!'
    print("All assertions passed.")