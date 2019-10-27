C = int(input())
box = []
for _ in range(C):
    A = list(map(int, input().split()))
    A.sort()
    box.append(A)

ans = [0, 0, 0]
for b in box:
    for i, b in enumerate(b):
        ans[i] = max(ans[i], b)

print(ans[0] * ans[1] * ans[2])