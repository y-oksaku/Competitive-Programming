N, M = map(int, input().split())

Tone = M * 1900 + (N - M) * 100
Pone = 1.0 / 2**M
prob = 1 - 1.0 / 2**M

ans = 1
for time in range(2, 100000):
    ans += prob * time
    prob *= (1.0 - Pone)

print(int(ans * Tone * Pone + 0.5))