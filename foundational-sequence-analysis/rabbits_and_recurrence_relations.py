# FIB: Rabbits and Recurrence Relations

def dynamic_programmed(filepath: str) -> int:
    with open(filepath, "r", encoding="utf-8") as f:
        sequence = f.read().strip()
        n, k = sequence.split(" ")
        n = int(n)
        k = int(k)
        if n > 40 or k > 5:
            raise ValueError
        F_at1 = 1
        F_at2 = F_at1
        Fmonth = 1
        newgen = 0
        for month in range(2, n):
            if month == 2:
                newgen = F_at2 * k
                Fmonth = F_at2 + newgen
            else:
                newgen = (Fmonth - newgen) * k
                Fmonth = Fmonth + newgen
        return Fmonth


if __name__ == "__main__":
    results = dynamic_programmed("rosalind_iprb.txt")
    print(results)
