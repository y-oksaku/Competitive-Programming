N = int(input())
S = input()

def isOk(first, second):
    prev, now = first, second
    ret = [prev]

    for s in S[1:] + S[0]:
        ret.append(now)
        isSame = (s == 'o')

        if isSame == now:
            prev, now = now, prev
        else:
            prev, now = now, not prev

    return ret if (first == prev and second == now) else []

for first in [True, False]:
    for second in [True, False]:
        ans = isOk(first, second)
        if ans:
            print(''.join(['S' if a else 'W' for a in ans[:-1]]))
            exit()

print('-1')
