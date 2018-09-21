from collections import defaultdict
import string

class TextAnalyzer(object):

    '''
    Take a text, parses it into sentences, and store the occurences and count of each word.
    '''
    def __init__(self, text):
        self.translator = str.maketrans('', '', string.punctuation)
        self.sentences = self._get_sentences(text)
        self.word_bank = defaultdict(int)
        self.avg_sentence_length = 0

    '''
    Get the number of occurences of a word in the text.
    '''
    def get_count(self, word):
        return self.word_bank[word]

    def _get_sentences(self, text):
        sentences = list()
        with open(text, 'r') as f:
            data = f.readlines()
            for line in data:
                line = line.rstrip()
                if line == '':
                    continue
                # TODO: handle more edge cases. These are used heavily in Austen.
                line = line.replace('Mr.', 'Mister')
                line = line.replace('Mrs.', 'Misses')
                sen = line.split('.')
                sentences = sentences + sen
        return self._filter_sentences(sentences)

    def _filter_sentences(self, sentences):
        for i, s in enumerate(sentences):
            if len(s) <= 1:
                del sentences[i]
            else:
                # Remove extraneous punctuation
                sentences[i] = s.translate(self.translator)
        return sentences

    def _get_wordbank(self, sentences):
        return
