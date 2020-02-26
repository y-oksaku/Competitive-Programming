N = int(input())
A = list(map(int, input().split()))

def calc(center):
    ret = 0
    for a in A:
        ret += (a - center)**2
    return ret

ans = 10**10
for c in range(min(A), max(A) + 1):
    ans = min(ans, calc(c))

print(ans)