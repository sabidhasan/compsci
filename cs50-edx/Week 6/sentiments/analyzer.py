from nltk.tokenize import TweetTokenizer

tknzr = TweetTokenizer()

class Analyzer():
    """Implements sentiment analysis."""

    def __init__(self, positives, negatives):
        """Initialize Analyzer."""
        #gets file of positives and negs. Lets bujild a dict
        self.res = {}
        with open(positives) as f:
            for line in f.readlines():
                if line[0] and line[0] != ";":
                    self.res[line.strip()] = 1

        with open(negatives) as f:
            for line in f.readlines():
                if line[0] and line[0] != ";":
                    self.res[line.strip()] = -1
        # TODO

    def analyze(self, text):
        """Analyze text for sentiment, returning its score."""
        tot = 0
        
        for word in tknzr.tokenize(text):
            if self.res.get(word):
                tot += self.res[word]
        return tot