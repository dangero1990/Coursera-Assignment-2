def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna)

def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    if len(dna1) > len(dna2):
        return True
    else:
        return False

def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    num_of_occurances = 0

    for char in dna:
        if char in nucleotide:
            num_of_occurances = num_of_occurances + 1

    return num_of_occurances

def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """

    for char in dna1:
        if dna2 in dna1:
            return True

    else:
        return False

def is_valid_sequence(dna):
    """ (str) -> bool

    Examines a string to determine if the string is a potiental DNA sequence.
    Returns True if the string provided only contains A, T, C, or G. Returns False
    if the provided string contains anything else outside the parameters.
    
    >>> is valid_sequence: 'ACGT'
    True
    >>> is valid_sequence: 'FCGT'
    False
    """

    non_nuc = 0
    for char in dna:
        if not char in 'ATCG':
            non_nuc = non_nuc + 1
    if non_nuc == 0:
        return True
    else:
        return False

def insert_sequence(dna1, dna2, index):
    """ (str, str, int) -> str

    Returns a string with dna2 inserted into dna1 at the given point specified
    with the integar index.

    >>> insert_sequence('CCGG', 'AT', 2):
    CCATGG
    >>> insert_sequence('CATG', 'TG', 3):
    CATGTG
    """
    sequence = dna1[: index] + dna2 + dna1[index:]
    if index > len(dna1):
        index == len(dna1)
    else:
        index == index
    return sequence

def get_complement(nucleotide):
    """ (str) - str

    Returns the complementary nucleotide for the given string.

    >>> get_complement('A')
    'T'
    >>> get_complement('G')
    'C'
    """
    s = nucleotide
    result = ''

    for char in s:
        if char is 'A':
            result = result + 'T'
        if char is 'T':
            result = result + 'A'
        if char is 'G':
            result = result + 'C'    
        if char is 'C':
            result = result + 'G'

        return result

def get_complementary_sequence(dna_sequence):
    """ (str) -> str
    
    Returns the string for the complementary sequence from the string DNA
    sequence provided.

    >>>get_complementary_sequence('ATG')
    'TAC'
    >>>get_complementary_sequence('TCA')
    'AGT'
    """

    d = dna_sequence
    result = ''

    for char in d:
        result = result + get_complement(char)

    return result