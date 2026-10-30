# CONS: Consensus and Profile

def consensus_analysis(filepath: str):
    with open(filepath, 'r', encoding='utf-8') as f:
        file_seq = f.readlines()
        sequences = {}

        for line in file_seq:
            line = line.strip()
            if line.startswith(">"):
                current_seq = sequences[line.lstrip(">")] = []
            else:
                current_seq.append(line)

        profile = {"A": {},
                   "C": {},
                   "G": {},
                   "T": {}
                   }
        seqs = ["".join(s) for s in sequences.values()]
        seq_length = len(next(iter(seqs)))
        for char in profile:
            for i in range(seq_length):
                profile[char][i] = 0

        for seq in sequences.values():
            seq = "".join(seq)
            for i in range(len(seq)):
                nucleotide = seq[i]
                profile[nucleotide][i] += 1

        consensus = []
        for i in range(seq_length):
            best = max("ACGT", key=lambda b: profile[b][i])
            consensus.append(best)
        print((", ".join(consensus)).replace(", ", ""))
        for key in profile:
            print(f"{key}:", *profile[key].values())


if __name__ == "__main__":
    results = consensus_analysis("rosalind_cons.txt")
