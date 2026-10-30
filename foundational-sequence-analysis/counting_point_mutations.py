# HAMM: Counting Point Mutations

def counting_mutations(filepath: str) -> int:
    with open(filepath, 'r', encoding='utf-8') as f:
        s, t = (f.read().strip().upper()).split("\n")
        mutations = 0
        for nucleotide in range(len(s)):
            if s[nucleotide] != t[nucleotide]:
                mutations += 1
        return mutations


if __name__ == "__main__":
    results = counting_mutations("rosalind_hamm.txt")
    print(results)
