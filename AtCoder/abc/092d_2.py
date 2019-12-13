A, B = map(int, input().split())
ans = [[False] * 100 for _ in range(50)] + [[True] * 100 for _ in range(50)]
A -= 1
B -= 1

for h in range(0, 50, 2):
    for w in range(0, 100, 2):
        if A > 0:
            ans[h][w] = True
            A -= 1

for h in range(51, 100, 2)[:: -1]:
    for w in range(0, 100, 2):
        if B > 0:
            ans[h][w] = False
            B -= 1

print(100, 100)
for line in ans:
    a = ['.' if s else '#' for s in line]
    print(''.join(a))