def gen_one_triple(n):
    result = []
    if n % 2 != 0:
        a = n
        b = ((n ** 2) / 2) - 0.5
        c = ((n ** 2) / 2) + 0.5
        result.extend([int(a), int(b), int(c)])
    else:
        a = n
        b = ((n / 2) ** 2) - 1
        c = ((n / 2) ** 2) + 1
        result.extend([int(a), int(b), int(c)])
    print(result)


def gen_multiple_triples(n):
    results = []
    for i in range(3, n + 1):
        if i % 2 != 0:
            a = i
            b = ((i ** 2) / 2) - 0.5
            c = ((i ** 2) / 2) + 0.5
            if b.is_integer() and c.is_integer(): results.extend([[int(a), int(b), int(c)]])
        else:
            a = i
            b = ((i / 2) ** 2) - 1
            c = ((i / 2) ** 2) + 1
            if b.is_integer() and c.is_integer(): results.extend([[int(a), int(b), int(c)]])
    for j, triple in enumerate(results):
        if j == 0:
            continue
        else:
            prev_triple = results[j - 1]
            if all(x in prev_triple for x in triple):
                results.pop(j)
                continue
    for triple in results:
        print(triple)


choice = input("1) Generate a triple for a value\n2) Generate first 'x' number of triples\nEnter index of choice: ")
if choice == '1':
    n = int(input('Enter number to generate pythogorean triples: '))
    gen_one_triple(n)
elif choice == '2':
    n = int(input('Enter number of pythogorean triples to generate: '))
    gen_multiple_triples(n)
