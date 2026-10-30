# RNA: Transcribing DNA into RNA

def dna_transcribing(filepath: str) -> str:
    with open(filepath, "r", encoding="utf-8") as f:
        sequence = f.read().strip().upper()
        rna_seq = sequence.replace("T", "U")
        return (rna_seq)


if __name__ == "__main__":
    results = dna_transcribing("rosalind_rna.txt")
    print(results)
