def calc(num):
    result = []
    if num % 2 != 0:
        a = num
        b = ((num**2)/2) - 0.5
        c = ((num**2)/2) + 0.5
        result.extend([int(a), int(b), int(c)])
    else:
        a = num
        b = ((num/2)**2) - 1
        c = ((num / 2)**2) + 1
        result.extend([int(a), int(b), int(c)])
    print(result)
num = int(input('Enter number to generate pythogorean triples: '))
calc(num)