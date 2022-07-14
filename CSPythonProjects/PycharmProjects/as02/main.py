"""
Functions that will intake rNA and convert to a string of corresponding proteins
"""



def make_dictionary():
    raw_dna = open('/Users/bridg3r/PycharmProjects/as02/aminodataset')
    dna_list = raw_dna.readlines()
    amino_dictionary = {}
    for i in dna_list:  # iterate through the list
        j = i.split(' ')  # create a inner list from the current element of the outer list
        key = j[0].replace('T', 'U')  # convert rNA codon to a DNA codon
        value = j[2]
        amino_dictionary[key] = value
    return amino_dictionary


def prot(rna: str) -> str:
    try:
        assert (len(rna) % 3 == 0) and (len(rna) >= 36)  # string has 12 or more codons
        assert amino[rna[-3] + rna[-2] + rna[-1]] == 'O'  # last codon is stop codon
        assert amino[rna[0] + rna[1] + rna[2]] == 'M'  # first codon is a start codon
        protein_string = ''
        for index, item in enumerate(rna, 0):  # convert RNA string into proteins
            if index % 3 == 0:
                if amino[item + rna[index + 1] + rna[index + 2]] == 'O':
                    assert len(protein_string) == (len(rna) / 3) - 1  # no early termination
                    return protein_string
                else:
                    a = protein_string.join(amino[item + rna[index + 1] + rna[index + 2]])
                    protein_string += a
    except (AssertionError, KeyError, TypeError):
        return None


def potential_proteins(rna):
    rna = rna.replace('T', 'U')
    pot_pros = []
    for index, item in enumerate(rna):
        if rna[index:index + 3] == 'AUG':
            for j in range(index + 3, len(rna), 3):
                if rna[j:j + 3] in ('UAG', 'UAA', 'UGA'):
                    a = prot(rna[index:j + 3])
                    if a is not None:
                        pot_pros.append(a)
                        break
    return pot_pros


amino = make_dictionary()



'''
def make_dictionary():
    raw_dna = open('/Users/bridg3r/PycharmProjects/as02/aminodataset')
    dna_list = raw_dna.readlines()
    amino_dictionary = {}
    for i in dna_list:  # iterate through the list
        j = i.split(' ')  # create a inner list from the current element of the outer list
        key = j[0].replace('T', 'U')  # convert rNA codon to a DNA codon
        value = j[2]
        amino_dictionary[key] = value
    return amino_dictionary


def prot(rna):
    try:
        assert (len(rna) % 3 == 0) and (len(rna) >= 36)  # string has 12 or more codons
        assert amino[rna[-3] + rna[-2] + rna[-1]] == 'O'  # last codon is stop codon
        assert amino[rna[0] + rna[1] + rna[2]] == 'M'  # first codon is a start codon
        protein_string = ''
        for index, item in enumerate(rna, 0):  # convert RNA string into proteins
            if index % 3 == 0:
                if amino[item + rna[index + 1] + rna[index + 2]] == 'O':
                    assert len(protein_string) == (len(rna) / 3) - 1  # no early termination
                    return protein_string
                else:
                    a = protein_string.join(amino[item + rna[index + 1] + rna[index + 2]])
                    protein_string += a
    except (AssertionError, KeyError, TypeError):
        return None


def potential_proteins(rna):
    rna = rna.replace('T', 'U')
    pot_pros = []
    for index in range(0, len(rna)):
        if rna[index:index + 3] == 'AUG':
            for j in range(0, len(rna[index + 3:]), 3):
                if rna[j:j + 3] in ('UAG', 'UAA', 'UGA'):
                    print(rna[index:j + 3])
                    a = prot(rna[index:j + 3])
                    if a is not None:
                        pot_pros.append(a)
    return pot_pros


def potential_proteins1(rna):
    rna = rna.replace('T', 'U')
    start_indices = []
    stop_indices = []
    for i in range(0, len(rna), 3):
        d = rna[i:i + 3]
        if d == 'AUG':
            start_indices.append(i)
        if d in ('UAG', 'UAA', 'UGA'):
            stop_indices.append(i + 3)
    start_stop = []
    for i in start_indices:  # create a list of start to stop sequences
        for j in stop_indices:
            if j > i + 4:
                rna[index:j + 3]
                a = rna[i:j]
                if prot(a) is not None:
                    start_stop.append(prot(a))
                break
    return start_stop

'''

amino = make_dictionary()
potential_proteins('AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGCTTCTGAACTGGTTACCTGCCGTGAGTAAATTAAAATTTTATTGACTTAGGTCACTAAATACTTTAACCAATATAGGCATAGCGCACAGACAGATAAAAATTACAGAGTACACAACATCCATGAAACGCATTAGCACCACCATTACCACCACCATCACCATTACCACAGGTAACGGTGCGGGCTGACGCGTACAGGAAACACAGAAAAAAGCCCGCACCTGACAGTGCGGGCTTTTTTTTTCGACCAAAGGTAACGAGGTAACAACCATGCGAGTGTTGAAGTTCGGCGGTACATCAGTGGCAAATGCAGAACGTTTTCTGCGTGTTGCCGATATTCTGGAAAGCAATGCCAGGCAGGGGCAGGTGGCCACCGTCCTCTCTGCCCCCGCCAAAATCACCAACCACCTGGTGGCGATGATTGAAAAAACCATTAGCGGCCAGGATGCTTTACCCAATATCAGCGATGCCGAACGTATTTTTGCCGAACTTTTGACGGGACTCGCCGCCGCCCAGCCGGGGTTCCCGCTGGCGCAATTGAAAACTTTCGTCGATCAGGAATTTGCCCAAATAAAACATGTCCTGCATGGCATTAGTTTGTTGGGGCAGTGCCCGGATAGCATCAACGCTGCGCTGATTTGCCGTGGCGAGAAAATGTCGATCGCCATTATGGCCGGCGTATTAGAAGCGCGCGGTCACAACGTTACTGTTATCGATCCGGTCGAAAAACTGCTGGCAGTGGGGCATTACCTCGAATCTACCGTCGATATTGCTGAGTCCACCCGCCGTATTGCGGCAAGCCGCATTCCGGCTGATCACATGGTGCTGATGGCAGGTTTCACCGCCGGTAATGAAAAAGGCGAACTGGTGGTGCTTGGACGCAACGGTTCCGACTACTCTGCTGCGGTGCTGGCTGCCTGTTTACGCGCCGATTGTTGCGAGATTTGGACGGACGTTGACGGGGTCTATACCTGCGACCCGCGTCAGGTGCCCGATGCGAGGTTGTTGAAGTCGATGTCCTACCAGGAAGCGATGGAGCTTTCCTACTTCGGCGCTAAAGTTCTTCACCCCCGCACCATTACCCCCATCGCCCAGTTCCAGATCCCTTGCCTGATTAAAAATACCGGAAATCCTCAAGCACCAGGTACGCTCATTGGTGCCAGCCGTGATGAAGACGAATTACCGGTCAAGGGCATTTCCAATCTGAATAACATGGCAATGTTCAGCGTTTCTGGTCCGGGGATGAAAGGGATGGTCGGCATGGCGGCGCGCGTCTTTGCAGCGATGTCACGCGCCCGTATTTCCGTGGTGCTGATTACGCAATCATCTTCCGAATACAGCATCAGTTTCTGCGTTCCACAAAGCGACTGTGTGCGAGCTGAACGGGCAATGCAGGAAGAGTTCTACCTGGAACTGAAAGAAGGCTTACTGGAGCCGCTGGCAGTGACGGAACGGCTGGCCATTATCTCGGTGGTAGGTGATGGTATGCGCACCTTGCGTGGGATCTCGGCGAAATTCTTTGCCGCACTGGCCCGCGCCAATATCAACATTGTCGCCATTGCTCAGGGATCTTCTGAACGCTCAATCTCTGTCGTGGTAAATAACGATGATGCGACCACTGGCGTGCGCGTTACTCATCAGATGCTGTTCAATACCGATCAGGTTATCGAAGTGTTTGTGATTGGCGTCGGTGGCGTTGGCGGTGCGCTGCTGGAGCAACTGAAGCGTCAGCAAAGCTGGCTGAAGAATAAACATATCGACTTACGTGTCTGCGGTGTTGCCAACTCGAAGGCTCTGCTCACCAATGTACATGGCCTTAATCTGGAAAACTGGCAGGAAGAACTGGCGCAAGCCAAAGAGCCGTTTAATCTCGGGCGCTTAATTCGCCTCGTGAAAGAATATCATCTGCTGAACCCGGTCATTGTTGACTGCACTTCCAGCCAGGCAGTGGCGGATCAATATGCCGACTTCCTGCGCGAAGGTTTCCACGTTGTCACGCCGAACAAAAAGGCCAACACCTCGTCGATGGATTACTACCATCAGTTGCGTTATGCGGCGGAAAAATCGCGGCGTAAATTCCTCTATGACACCAACGTTGGGGCTGGATTACCGGTTATTGAGAACCTGCAAAATCTGCTCAATGCAGGTGATGAATTGATGAAGTTCTCCGGCATTCTTTCTGGTTCGCTTTCTTATATCTTCGGCAAGTTAGACGAAGGCATGAGTTTCTCCGAGGCGACCACGCTGGCGCGGGAAATGGGTTATACCGAACCGGACCCGCGAGATGATCTTTCTGGTATGGATGTGGCGCGTAAACTATTGATTCTCGCTCGTGAAACGGGACGTGAACTGGAGCTGGCGGATATTGAAATTGAACCTGTGCTGCCCGCAGAGTTTAACGCCGAGGGTGATGTTGCCGCTTTTATGGCGAATCTGTCACAACTCGACGATCTCTTTGCCGCGCGCGTGGCGAAGGCCCGTGATGAAGGAAAAGTTTTGCGCTATGTTGGCAATATTGATGAAGATGGCGTCTGCCGCGTGAAGATTGCCGAAGTGGATGGTAATGATCCGCTGTTCAAAGTGAAAAATGGCGAAAACGCCCTGGCCTTCTATAGCCACTATTATCAGCCGCTGCCGTTGGTACTGCGCGGATATGGTGCGGGCAATGACGTTACAGCTGCCGGTGTCTTTGCTGATCTGCTACGTACCCTCTCATGGAAGTTAGGAGTCTGACATGGTTAAAGTTTATGCCCCGGCTTCCAGTGCCAATATGAGCGTCGGGTTTGATGTGCTCGGGGCGGCGGTGACACCTGTTGATGGTGCATTGCTCGGAGATGTAGTCACGGTTGAGGCGGCAGAGACATTCAGTCTCAACAACCTCGGACGCTTTGCCGATAAGCTGCCGTCAGAACCACGGGAAAATATCGTTTATCAGTGCTGGGAGCGTTTTTGCCAGGAACTGGGTAAGCAAATTCCAGTGGCGATGACCCTGGAAAAGAATATGCCGATCGGTTCGGGCTTAGGCTCCAGTGCCTGTTCGGTGGTCGCGGCGCTGATGGCGATGAATGAACACTGCGGCAAGCCGCTTAATGACACTCGTTTGCTGGCTTTGATGGGCGAGCTGGAAGGCCGTATCTCCGGCAGCATTCATTACGACAACGTGGCACCGTGTTTTCTCGGTGGTATGCAGTTGATGATCGAAGAAAACGACATCATCAGCCAGCAAGTGCCAGGGTTTGATGAGTGGCTGTGGGTGCTGGCGTATCCGGGGATTAAAGTCTCGACGGCAGAAGCCAGGGCTATTTTACCGGCGCAGTATCGCCGCCAGGATTGCATTGCGCACGGGCGACATCTGGCAGGCTTCATTCACGCCTGCTATTCCCGTCAAUGGCCTGAGCTTGCCGCGAAGCTGATGAAAGATGTTATCGCTGAACC')
#potential_proteins('AUGCAGCAGAUGCAGCAGCAGCACAGCAGCAGCAGCAGCAGCCAGCAGCAGCAGCAGCAGCAGUAGCAGCAGCAGCAGCAGAUGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGUAGCAGUAG')
print(potential_proteins('AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'))


