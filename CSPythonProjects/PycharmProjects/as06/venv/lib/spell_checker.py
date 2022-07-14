"""
A simple spell-checker for demonstrating the membership operation in Python's built-in collections.

Try varying:
  Container types with input from file /srv/datasets/us-constitution.txt
  Set containers given input files /srv/datasets/{joyce-ulysses.txt,tolstoy-anna-karenina.txt}
  Containers and input files /srv/datasets/{genius.txt,bill-of-rights.txt}
"""
from __future__ import annotations

__author__ = 'Jeffrey Bergamini for CSE 30, jbergami@ucsc.edu'

import re
import sys
import time
from collections.abc import Callable, Container, Iterable


def load_dictionary(collection_type: Callable, dict_path: str) -> Container[str]:
    """
    Populates a container with a simple spell-checking sp_dictionary (one word per line).

    :param collection_type: the type of collection to populate
    :param dict_path: the path to the sp_dictionary file
    :return: the populated container
    """
    with open(dict_path) as dict_file:
        return collection_type(line.strip().lower() for line in dict_file)


def misspelled_words(dictionary: Container[str], words: Iterable[str]) -> list[str]:
    """
    Finds and returns all misspelled words.

    :param dictionary: a container supporting membership test (in)
    :param words: the words to spell-check
    :return: a list containing all words not in dictionary, in the order encountered
    """
    return [word for word in words if word and word not in dictionary]


def spell_check(dictionary_type: Callable, dict_path: str, to_check: Iterable[str]):
    before_load = time.perf_counter()
    dictionary = load_dictionary(dictionary_type, dict_path)
    after_load = time.perf_counter()
    before_check = time.perf_counter()
    misspelled = misspelled_words(dictionary, to_check)
    after_check = time.perf_counter()
    if misspelled:
        print('\n'.join(misspelled))
    print(f'''Collection type: {dictionary_type}
Dictionary path: {dict_path}
Words in dictionary: {len(dictionary)}
Dictionary load time: {after_load - before_load:f}
Words in text: {len(to_check)}
Spell-check time: {after_check - before_check:f}''',
          file=sys.stderr)


'''
if __name__ == '__main__':
    # First command-line arg (if present) is the name of a built-in collection type
    available_containers = {cls.__name__: cls for cls in (tuple, list, set, frozenset)}
    container_type = available_containers[sys.argv[1]] if len(sys.argv) > 1 and sys.argv[1] in \
                                                          available_containers else set
    # Second command-line arg (if present) is the path to a spell-checking dictionary file
    dict_file_path = sys.argv[2] if len(sys.argv) > 2 else '/srv/datasets/many-english-words.txt'
    # Use a regular expression to compose a list of each "word" in stdin
    # See: https://docs.python.org/3/library/re.html#regular-expression-syntax
    all_words = [word for word in re.split(r"[^\w']+", sys.stdin.read().lower()) if word]
    spell_check(container_type, dict_file_path, all_words)
    '''