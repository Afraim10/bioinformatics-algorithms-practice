# IPRB: Mendel's First Law

def calc(filepath: str):
    with open(filepath, 'r', encoding='utf-8') as f:
        numbers = f.read().strip()
        k, m, n = numbers.split(" ")
        k = int(k)  # HH
        m = int(m)  # Hh
        n = int(n)  # hh
        total = k + m + n
        hetero_hetero = (m/total) * ((m-1)/(total-1))
        hetero_homorecess = 2 * ((m/total) * (n/(total-1)))
        homorecess_homorecess = (n/total) * ((n-1)/(total-1))
        dominant_pheno_p = 1 - \
            ((1*homorecess_homorecess) + (0.50 *
             hetero_homorecess) + (0.25 * hetero_hetero))
        return dominant_pheno_p


if __name__ == "__main__":
    results = calc("rosalind_iprb.txt")
    print(results)
