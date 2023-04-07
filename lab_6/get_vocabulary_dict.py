import csv

from typing import Dict


def get_vocabulary_dict() -> Dict[int, str]:
    """Read the fixed vocabulary list from the datafile and return.

    :return: a dictionary of words mapped to their indexes
    """

    # FIXME: Parse data from the 'data/vocab.txt' file.
    # - The file is saved in tab-separated values (TSV) format.
    # - Each line contains a word's ID and the word itself.
    # The output dictionary should map word's ID on the word itself, e.g.:
    #   {1: 'aa', 2: 'ab', ...}
    dictionary = {}
    with open('data/vocab.txt', newline="") as file:
        read = csv.reader(file, delimiter='\t')
        for row in read:
            dictionary[int(row[0])] = row[1]
    file.close()
    return dictionary

