import sys
sys.setrecursionlimit(10 ** 7)

Q = []
H = set(range(8))
W = set(range(8))
for h in range(8):
    for w, s in enumerate(input()):
        if s == 'Q':
            Q.append((h, w))
            if not h in H or not w in W:
                print('No Answer')
                exit()
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

def search(state, H, W):
    if len(state) == 8:
        if isOk(state):
            printQ(state)
            exit()
        return
    for h in H:
        for w in W:
            newH = H.copy()
            newH.remove(h)
            newW = W.copy()
            newW.remove(w)
            search(state + [(h, w)], newH, newW)

search(Q, H, W)
print('No Answer')
