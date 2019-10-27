V = list(map(int, input().split()))

def f(A, B, C):
    ret = 0
    for v in V:
        cnt = float('inf')
        for a in range(v // A + 1):
            for b in range(v // B + 1):
                l = A * a + B * b
                if (v - l) >= 0 and (v - l) % C == 0:
                    cnt = min(cnt, a + b + (v - l) // C)
        ret += cnt
    return ret

ans = float('inf')
for a in range(1, 31):
    for b in range(1, 31):
        for c in range(1, 31):
            ans = min(ans, f(a, b, c))

print(ans)