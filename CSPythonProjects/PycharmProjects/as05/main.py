"""
Utility module for dealing with readability metrics of English text.
"""
from __future__ import annotations

__author__ = 'A student in CSE 30, someone@ucsc.edu'

import math
import re

# The syllable dictionary will only be created one time
masterlist = open('/Users/bridg3r/Library/Containers/com.apple.mail/Data/Library/Mail Downloads/E98C6771-4A63-43D5-A7D0-52812391D34D/syllables.txt')
syllist = masterlist.readlines()  # create a list of all the words with ';'
syldict = {}
for theword in syllist:
    theword = theword.replace('\n', '')
    counter = theword.count(';') + 1 + theword.count('-')
    if theword.replace(';', '') in syldict and counter < syldict[theword.replace(';', '')]:
        continue
    else:
        syldict[theword.replace(';', '')] = counter


class Readability(str):
    """
    Represents a string that can be assessed for readability metrics of English text.
    """

    def __init__(self, words1):
        self.words1 = words1
        super().__init__()  # text = 'hello world'
        self._words = self.words()
        self.word_count = len(self._words)
        self._sentences = self.sentences()
        self.sentence_count = len(self._sentences)
        self._num_syllables = self.num_syllables()
        self._character_count = self.character_count()
        self._polysyllabic_words = self.polysyllabic_words()
        self.poly_count = len(self._polysyllabic_words)

    def words(self):
        raw_list = re.split("[^A-Za-z0-9'-]", self)  # make list of all words
        return [t for t in raw_list if t]

    def sentences(self):
        wordspunct = self.split()  # make a list of words and punctuation
        sentence = ''
        all_sentences = []
        ends = ('?', '!', '.',
                "'?", '"?', ')?', '?"', "?'", "?)",
                "'!", '"!', ')!', '!"', "!'", "!)",
                "'.", '".', ').', '."', ".'", ".)")
        for i in wordspunct:  # build a list one sentence at a time
            if sentence == '':  # No space if its the beginning
                sentence += i
            else:
                sentence += ' ' + i
            if (i[-1] in ends[:3]) or (len(i) > 1 and i[-2:] in ends[3:]):
                all_sentences.append(sentence)
                sentence = ''
        return all_sentences

    def num_syllables(self):
        syllables = 0
        for i in self._words:
            i = i.lower()
            try:
                syllables += syldict[i]
            except KeyError:
                syllables += 1
        return syllables

    def character_count(self):
        count = 0
        for i in self:
            if i.isalpha() or i.isdigit():
                count += 1
        return count

    def polysyllabic_words(self):
        total_polysyllables = []
        for i in self._words:
            i = i.lower()
            if i in syldict and (syldict[i] >= 3):
                total_polysyllables.append(i)
        return total_polysyllables

    def automated_readability_index(self):
        """
        Calculates and returns the automated readability index of this text.
        See: https://en.wikipedia.org/wiki/Automated_readability_index
        """
        return 4.71 * (self._character_count / self.word_count) \
               + 0.5 * (self.word_count / self.sentence_count) - 21.43

    def coleman_liau_index(self):
        """
        Calculates and returns the Coleman–Liau index of this text.
        See: https://en.wikipedia.org/wiki/Coleman%E2%80%93Liau_index
        L is the average number of letters per 100 words
        and S is the average number of sentences per 100 words.
        """
        L = self._character_count / self.word_count * 100
        S = self.sentence_count / self.word_count * 100
        return 0.0588 * L - 0.296 * S - 15.8

    def flesch_kincaid_grade(self):
        """
        Calculates and returns the Flesch–Kincaid grade level of this text.
        See: https://en.wikipedia.org/wiki/Flesch%E2%80%93Kincaid_
        readability_tests#Flesch%E2%80%93Kincaid_grade_level
        """
        return 0.39 * (self.word_count / self.sentence_count) + 11.8 \
               * (self._num_syllables / self.word_count) - 15.59

    def smog_grade(self) -> float or None:
        """
        Calculates and returns the SMOG grade of this text,
        or None if the text contains fewer than 30 sentences.
        See: https://en.wikipedia.org/wiki/SMOG
        """

        if self.sentence_count >= 30:
            return 1.0430 * math.sqrt(self.poly_count * 30 / self.sentence_count) + 3.1291
        else:
            return None


# demo = Readability('why hello there you "fella". what are you up to today? How is school going for ya? Are you getting good grades?')
# demo = Readability('hello world')
ind = open('/Users/bridg3r/Library/Containers/com.apple.mail/Data/Library/Mail Downloads/B8596F2E-8740-45BE-AA6B-2D27A700F43B/declaration-of-independence.txt')
dec = ind.read()
demo = Readability(dec)
if __name__ == '__main__':
    # demo = Readability(sys.stdin.read())
    # My solution has methods words() and sentences() which return lists of all words and sentences.
    # You don't have to implement these, but I recommend it.
    if hasattr(demo, 'words'):
        print(len(demo.words()), 'words: ', demo.words()[:5], '...')
    if hasattr(demo, 'sentences'):
        print(len(demo.sentences()), 'sentences: ', demo.sentences()[:5], '...')
    if hasattr(demo, 'num_syllables'):
        print(demo.num_syllables(), 'syllables')
    if hasattr(demo, 'polysyllabic_words'):
        print(len(demo.polysyllabic_words()), 'polysyllabic words: ',
              demo.polysyllabic_words()[:5], '...')
    print('ARI', demo.automated_readability_index())
    print('CLI', demo.coleman_liau_index())
    print('FKG', demo.flesch_kincaid_grade())
    print('SMOG', demo.smog_grade())
