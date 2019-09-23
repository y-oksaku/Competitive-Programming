N = int(input())

def digitSum(n):
    return sum([int(s) for s in str(n)])

ans = digitSum(N - 1) + digitSum(1)
for a in range(1, N):
    b = N - a
    ans = min(ans, digitSum(a) + digitSum(b))

print(ans)