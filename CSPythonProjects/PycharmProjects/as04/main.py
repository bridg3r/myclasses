"""
Contains class Protein for working with protein-related information.
"""

__author__ = 'A student in CSE 30, someone@ucsc.edu'


class Protein:
    """ Represents an immutable sequence of amino acids. """

    def __init__(self, aminos=None):
        a = open('/Users/bridg3r/PycharmProjects/as04/proteinmass')
        b = a.readlines()
        self.amino_mass = {}
        self.amino_alphabet = []
        for i in b:  # iterate through the list
            j = i.split(' ')  # create a inner list from the current element of the outer list
            key = j[0]
            value = float(j[1])
            self.amino_mass[key] = value
            self.amino_alphabet.append(key)
        self.aminos = ''
        for i in aminos:
            if i not in self.amino_alphabet:
                raise ValueError('Invalid amino acid character: ' + i)
            self.aminos += i

    def __add__(self, addition):
        return Protein(self.aminos + str(Protein(addition)))

    def __eq__(self, other):
        return bool(self.aminos == str(Protein(other)))

    def __getitem__(self, key):
        if isinstance(key, slice):
            return Protein(self.aminos[key])
        else:
            return self.aminos[key]

    def __len__(self):
        """ Returns the length of this protein, i.e. its number of amino acids. """
        return len(self.aminos)

    def __repr__(self):
        """ Returns a string that would result in reproducing this protein when interpreted. """
        return "Protein" + "('" + self.aminos + "')"

    def __str__(self):
        """ Returns a string containing the amino-acid letters for this protein. """
        return self.aminos

    def mass(self):
        mass = 0
        for i in self.aminos:
            mass += self.amino_mass[i]
        return mass

