A, B = map(int, input().split())

ans = A - 1

if B >= A:
    ans += 1

print(ans)