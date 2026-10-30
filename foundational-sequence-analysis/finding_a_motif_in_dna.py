# SUBS: Finding a Motif in DNA


def motif_finder(filepath: str):
    with open(filepath, 'r', encoding='utf-8') as f:
        file_seq = f.readlines()
        dna, motif = file_seq[0].strip().upper(), file_seq[1].strip().upper()

        if len(motif) > len(dna):
            raise ValueError
        elif motif not in dna:
            raise ValueError
        location = []
        iter_motif_len = len(motif)
        dna_len = len(dna)
        for n in range(dna_len):
            if len(dna[n:n+iter_motif_len]) != len(motif):
                pass
            elif dna[n:n+iter_motif_len] == motif:
                location.append(n+1)
        return location


if __name__ == "__main__":
    results = motif_finder("rosalind_subs.txt")
    print(*results)
