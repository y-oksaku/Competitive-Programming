A, B, C = map(int, input().split())

ans = min(
    abs(A - B) + abs(B - C),
    abs(A - C) + abs(B - C),
    abs(B - A) + abs(A - C),
    abs(B - C) + abs(A - C),
    abs(C - A) + abs(A - B),
    abs(C - B) + abs(A - B),
)

print(ans)