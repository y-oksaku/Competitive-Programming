S = input()
N = len(S)
K = int(input())

if len(set(S)) == 1 or len(S) == 1:
    ans = K * len(S) // 2
    print(ans)
    exit()

left = 0
right = 1

while left < N and S[left] == S[0]:
    left += 1
while right <= N and S[-right] == S[-1]:
    right += 1
right -= 1

change = 0
isChanged = False
T = list(S[left: N - right])

for i, t in enumerate(T[1:], start=1):
    if t == T[i - 1]:
        if not isChanged:
            change += 1
            isChanged = True
            continue
    isChanged = False

ans = change * K
if S[0] == S[-1]:
    ans += left // 2 + (left + right) // 2 * (K - 1) + right // 2
else:
    ans += (left // 2 + right // 2) * K

print(ans)
