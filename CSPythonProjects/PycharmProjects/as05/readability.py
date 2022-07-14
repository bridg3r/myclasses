"""
Utility module for dealing with readability metrics of English text.
"""
from __future__ import annotations

__author__ = 'A student in CSE 30, someone@ucsc.edu'

import math
import re
import sys


class Readability(str):
    """
    Represents a string that can be assessed for readability metrics of English text.
    """

    def __init__(self):
        super().__init__()
        self.all_words
        self.all_sentences
        self.all_polysllabic_words
        self.num_characters
        self.num_syllables



    def automated_readability_index(self) -> float:
        """
        Calculates and returns the automated readability index of this text.
        See: https://en.wikipedia.org/wiki/Automated_readability_index
        """
        # TODO
        pass

    def coleman_liau_index(self) -> float:
        """
        Calculates and returns the Coleman–Liau index of this text.
        See: https://en.wikipedia.org/wiki/Coleman%E2%80%93Liau_index
        """
        # TODO
        pass

    def flesch_kincaid_grade(self) -> float:
        """
        Calculates and returns the Flesch–Kincaid grade level of this text.
        See: https://en.wikipedia.org/wiki/Flesch%E2%80%93Kincaid_readability_tests#Flesch%E2%80%93Kincaid_grade_level
        """
        # TODO
        pass

    def smog_grade(self) -> float | None:
        """
        Calculates and returns the SMOG grade of this text,
        or None if the text contains fewer than 30 sentences.
        See: https://en.wikipedia.org/wiki/SMOG
        """
        # TODO
        pass


if __name__ == '__main__':
    demo = Readability(sys.stdin.read())
    # My solution has some extra (helper) methods.
    # You don't have to implement these, but I recommend doing something like it.
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
