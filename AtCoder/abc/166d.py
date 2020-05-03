X = int(input())

for b in range(-10**6, 10**6):
    a5 = abs(b**5 + X)
    a = int(pow(a5, 1 / 5))

    if a5 < 0:
        a = -a

    if a**5 - b**5 == X:
        print(a, b)
        exit()
