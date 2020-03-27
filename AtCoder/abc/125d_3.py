N = int(input())
A = list(map(int, input().split()))
B = [abs(a) for a in A]

minus = sum([a < 0 for a in A])
ans = sum(B)

if minus % 2 == 1:
    ans -= min(B) * 2

print(ans)
