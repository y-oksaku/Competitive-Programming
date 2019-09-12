N = int(input())
A = [int(input()) for _ in range(N)]

# 操作2は0番目からの距離のmodが変化しない
# modが異なる数 / 2が答え

B = sorted(A)
sortedIndex = {b : i for i, b in enumerate(B)}

ans = 0
for i, a in enumerate(A):
    if i % 2 != sortedIndex[a] % 2:
        ans += 1

print(ans // 2)