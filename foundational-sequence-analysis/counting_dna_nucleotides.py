# DNA: Counting DNA Nucleotides

def nucleotide_counting(filepath: str) -> str:
    with open(filepath, 'r', encoding='utf-8') as f:
        sequence = f.read().strip().upper()
    counts = [sequence.count(nuc) for nuc in "ACGT"]
    return " ".join(map(str, counts))


if __name__ == "__main__":
    results = nucleotide_counting("rosalind_dna.txt")
    print(results)
