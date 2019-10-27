N = int(input())
words = [input() for _ in range(N)]

V = set([words[0]])

for i, w in enumerate(words[1:], start=1):
    if w[0] != words[i - 1][-1] or w in V:
        if i % 2 == 0:
            print('LOSE')
        else:
            print('WIN')
        break
    V.add(w)
else:
    print('DRAW')