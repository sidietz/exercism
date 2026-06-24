"""Module for creating DNA/RNA complements"""

MAPPING = {"G": "C", "C": "G", "T": "A", "A": "U"}

def to_rna(dna_strand):
    """
    Takes an dna_strand and retuns its complement
    """
    dna_list = list(dna_strand)
    complement_list = []

    for base in dna_list:
        complement = MAPPING[base]
        complement_list.append(complement)

    return "".join(complement_list)
