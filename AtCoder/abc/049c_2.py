S = input()[::-1]
W = [s[::-1] for s in ('dream', 'dreamer', 'erase', 'eraser')]

def isOk():
    now = 0
    while now < len(S):
        for w in W:
            if S[now: now + len(w)] == w:
                now += len(w)
                break
        else:
            return False
    return True

print('YES' if isOk() else 'NO')
