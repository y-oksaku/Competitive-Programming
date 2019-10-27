N = int(input())
A = list(map(int, input().split()))
B = [A[0]]

for a in A:
    if B[-1] != a:
        B.append(a)

N = len(B)
ans = 1
prev = -1
for i in range(1, N - 1):
    if B[i - 1] < B[i] and B[i + 1] < B[i]:
        if i - prev > 1:
            ans += 1
            prev = i
    elif B[i - 1] > B[i] and B[i + 1] > B[i]:
        if i - prev > 1:
            ans += 1
            prev = i

print(ans)