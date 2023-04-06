def gen_primes(n: int):
    D = {}
    for q in range(2, n + 1):
        if q not in D:
            print(q)
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]


gen_primes(int(input("Enter the limit for generating the primes: ")))
