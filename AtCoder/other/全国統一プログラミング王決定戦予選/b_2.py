N = int(input())
A = input()
B = input()
C = input()

ans = 0
for a, b, c in zip(A, B, C):
    if a == b == c:
        continue
    if len(set([a, b, c])) == 2:
        ans += 1
    else:
        ans += 2

print(ans)
