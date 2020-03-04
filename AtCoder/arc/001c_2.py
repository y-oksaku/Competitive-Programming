from itertools import permutations

Q = []
H = set(range(8))
W = set(range(8))

for h in range(8):
    for w, s in enumerate(input()):
        if s == 'Q':
            if not h in H or not w in W:
                print('No Answer')
                exit()
            Q.append((h, w))
            H.remove(h)
            W.remove(w)


def isOk(state):
    for i, (h, w) in enumerate(state):
        for u, v in state[i + 1:]:
            if h == u or w == v or (h - u) == (w - v) or (h - u) == -(w - v):
                return False
    return True

def printQ(state):
    Q = set(state)
    for h in range(8):
        for w in range(8):
            print('Q' if (h, w) in Q else '.', end='')
        print('')

H = list(H)
W = list(W)

for hs in permutations(range(5), r=5):
    for ws in permutations(range(5), r=5):
        state = Q + [(H[h], W[w]) for h, w in zip(hs, ws)]
        if isOk(state):
            printQ(state)
            exit()

print('No Answer')
