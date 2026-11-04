def to_rna(dna_strand):
    sequence = {"G": "C", "C": "G", "T": "A", "A": "U"}
    return "".join([sequence[k] for k in dna_strand])
