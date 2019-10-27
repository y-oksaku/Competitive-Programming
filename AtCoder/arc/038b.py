from collections import deque

H, W = map(int, input().split())

atlas = [[False for _ in range(W + 2)] for _ in range(H + 2)]

for h in range(1, H + 1):
    line = input()
    for w in range(1, W + 1):
        if line[w - 1] == '.':
            atlas[h][w] = True

memo = [[[-1, -1]for _ in range(W + 1)] for _ in range(H + 1)]
def search(h, w, player):
    if memo[h][w][player] != -1:
        return memo[h][w][player]

    if not (atlas[h + 1][w] or atlas[h][w + 1] or atlas[h + 1][w + 1]):
        if player == 0:
            return False
        else:
            return True

    if player == 0:
        ret = False
        if atlas[h + 1][w]:
            ret |= search(h + 1, w, 1)
        if atlas[h][w + 1]:
            ret |= search(h, w + 1, 1)
        if atlas[h + 1][w + 1]:
            ret |= search(h + 1, w + 1, 1)
    else:
        ret = True
        if atlas[h + 1][w]:
            ret &= search(h + 1, w, 0)
        if atlas[h][w + 1]:
            ret &= search(h, w + 1, 0)
        if atlas[h + 1][w + 1]:
            ret &= search(h + 1, w + 1, 0)
    memo[h][w][player] = ret
    return ret

ans = search(1, 1, 0)
if ans:
    print('First')
else:
    print('Second')