N = int(input())
S = input()

ans = 0
for i in range(1, N - 1):
    L = set(list(S[:i])) & set(list(S[i:]))
    ans = max(ans, len(L))
print(ans)