N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

top = 0
bot = sum(B)
ans = 0
for a, b in zip(A, B):
    top += a
    ans = max(ans, top + bot)
    bot -= b

print(ans)
