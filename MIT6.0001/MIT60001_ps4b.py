# Problem Set 4B

import string

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

def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("MIT60001_ps4_story.txt", "r")
    story = str(f.read())
    f.close()
    return story

WORDLIST_FILENAME = 'MIT60001_ps4_words.txt'

class Message(object):
    def __init__(self, text, load_word_dict=True):
        '''
        Initializes a Message object
        text (string): the message's text
        '''
        self.message_text = text
        if load_word_dict:
            self.valid_words = load_words(WORDLIST_FILENAME)

    def get_message_text(self):
        return self.message_text

    def get_valid_words(self):
        return self.valid_words[::]

    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift.
        
        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        ret = { l: chr(((ord(l) + shift - 97) % 26) + 97) for l in string.ascii_lowercase }
        for l in string.ascii_uppercase:
            ret[l] = chr(((ord(l) + shift - 65) % 26) + 65)
        return ret

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        shift_dictionary = self.build_shift_dict(shift)
        msg = list(self.message_text)
        for (i, letter) in enumerate(msg):
            if letter in shift_dictionary:
                msg[i] = shift_dictionary[letter]
        return ''.join(msg)

class PlaintextMessage(Message):
    def __init__(self, text, shift, load_word_dict=True):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message
        '''
        super().__init__(text, load_word_dict)
        self.shift = shift
        self.encryption_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        '''
        return self.shift

    def get_encryption_dict(self):
        '''
        Used to safely access a copy self.encryption_dict outside of the class
        '''
        self.encryption_dict.copy()

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift.        
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        self.__init__(self.message_text, shift, False)

class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
        text (string): the message's text
        '''
        super().__init__(text)

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create 
        the maximum number of valid words, you may choose any of those shifts 
        (and their corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        best_decryption = (0, "")
        max_matches = 0
        for i in range(1, 27):
            matched_words = 0
            for word in self.apply_shift(i).split(" "):
                if is_word(self.get_valid_words(), word):
                    matched_words += 1
            if matched_words > max_matches:
                max_matches = matched_words
                best_decryption = (i, self.apply_shift(i))
        return best_decryption if best_decryption[0] != 0 else (1, self.apply_shift(1))


if __name__ == '__main__':

#    #Example test case (PlaintextMessage)
    plaintext = PlaintextMessage('hello', 2)
    print('Expected Output: jgnnq')
    assert plaintext.get_message_text_encrypted() == 'jgnnq'

    #Example test case (CiphertextMessage)
    ciphertext = CiphertextMessage('jgnnq')
    print('Expected Output:', (24, 'hello'))
    assert ciphertext.decrypt_message()[1] == 'hello'

    story_text = get_story_string()
    print(CiphertextMessage(story_text).decrypt_message()[1])    
