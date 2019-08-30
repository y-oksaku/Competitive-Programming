from functools import lru_cache

W, H = map(int, input().split())
N = int(input())

M = [tuple(map(int, input().split())) for _ in range(N)]

@lru_cache(maxsize=None)
def search(L, R, U, D):
    maxGold = 0
    for x, y in M:  # 次に使うマシーン
        if not(L <= x <= R and D <= y <= U):
            continue
        gold = (R - L + 1) + (U - D + 1) - 1

        gold += search(L, x - 1, U, y + 1)  # 左上
        gold += search(x + 1, R, U, y + 1)  # 右上
        gold += search(x + 1, R, y - 1, D)  # 右下
        gold += search(L, x - 1, y - 1, D)  # 左下

        maxGold = max(maxGold, gold)

    return maxGold

ans = search(1, W, H, 1)
print(ans)