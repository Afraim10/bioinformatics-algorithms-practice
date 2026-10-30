# PROT: Translating RNA into Protein


def translation(filepath: str):
    with open(filepath, 'r', encoding='utf-8') as f:
        mrna_sequence = f.read().strip().upper()
        table = rna_codon_table = {
            # U
            "UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
            "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
            "UAU": "Y", "UAC": "Y", "UAA": "", "UAG": "",
            "UGU": "C", "UGC": "C", "UGA": "", "UGG": "W",
            # C
            "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
            "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
            "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
            "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
            # A
            "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
            "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
            "AAU": "N", "AAC": "N", "AAG": "K", "AAA": "K",
            "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
            # G
            "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
            "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
            "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
            "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"
        }
        protein = []
        codons = [mrna_sequence[i:i+3]
                  for i in range(0, len(mrna_sequence), 3)]
        for codon in codons:
            protein.append(table[codon])
        return (", ".join(protein)).replace(", ", "")


if __name__ == "__main__":
    results = translation("rosalind_prot.txt")
    print(results)
