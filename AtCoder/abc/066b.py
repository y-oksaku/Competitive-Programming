S = input()

ans = 1
for right in range(2, len(S)):
    T = S[: right]
    if T == S:
        break
    if len(T) % 2 == 0 and T[: len(T) // 2] == T[len(T) // 2:]:
        ans = max(ans, len(T))

print(ans)
