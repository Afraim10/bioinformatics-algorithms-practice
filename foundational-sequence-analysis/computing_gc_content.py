# GC: Computing GC Content

def gc_computing(filepath: str) -> str:
    with open(filepath, "r", encoding="utf-8") as f:
        read = f.readlines()
        highest_gc = 0
        formatted = {}
        for line in read:
            line = line.strip()
            if line.startswith(">"):
                current_header = line.strip(">")
                formatted[current_header] = ""
            elif not line.startswith(">"):
                formatted[current_header] += line
        for seq in formatted:
            current_gc = ((str(formatted[seq]).count(
                "G")+str(formatted[seq]).count("C")) / len(formatted[seq])) * 100
            if current_gc > highest_gc:
                highest_gc = current_gc
                highest_gc_header = seq
        return f"{highest_gc_header}\n{highest_gc}"


if __name__ == "__main__":
    results = gc_computing("rosalind_gc.txt")
    print(results)
