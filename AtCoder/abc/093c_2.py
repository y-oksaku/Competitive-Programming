A, B, C = map(int, input().split())

A, B, C = sorted((A, B, C))
ans = 0

if sum([C % 2 == a % 2 for a in (A, B, C)]) == 2:
    ans += 1
    if A % 2 == C % 2:
        A += 1
    else:
        B += 1
    C += 1

ans += sum([C - a for a in (A, B, C)]) // 2
print(ans)