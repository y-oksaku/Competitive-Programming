N, A, B = map(int, input().split())
ans = 0

for _ in range(N):
    s, d = input().split()
    ans += max(A, min(int(d), B)) * (-1 if s[0] == 'W' else 1)

if ans == 0:
    print(0)
else:
    print('West' if ans < 0 else 'East', abs(ans))
