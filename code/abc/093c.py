A, B, C = map(int, input().split())

if A % 2 == B % 2 == C % 2:
    N = max(A, B, C)
    ans = (N - A) // 2 + (N - B) // 2 + (N - C) // 2
    print(ans)
else:
    if A % 2 == B % 2:
        A += 1
        B += 1
    elif B % 2 == C % 2:
        B += 1
        C += 1
    else:
        C += 1
        A += 1
    N = max(A, B, C)
    ans = 1 + (N - A) // 2 + (N - B) // 2 + (N - C) // 2
    print(ans)