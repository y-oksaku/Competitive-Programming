N = int(input())
A1 = list(map(int, input().split()))
A2 = list(map(int, input().split()))

ans = 0
now = 0
bot = sum(A2)

for a1, a2 in zip(A1, A2):
    now += a1
    ans = max(ans, now + bot)
    bot -= a2

print(ans)