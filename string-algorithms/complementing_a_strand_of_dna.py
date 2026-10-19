def dna_complementing(filepath: str) -> str:
    with open(filepath, "r", encoding="utf-8") as f:
        sequence = f.read().strip().upper()
        complementing_table = sequence.maketrans("ACGT", "TGCA")
        complemented = sequence.translate(complementing_table)
        reverse_complemented = "".join(reversed(complemented))
        return reverse_complemented


if __name__ == "__main__":
    results = dna_complementing("rosalind_revc.txt")
    print(results)
