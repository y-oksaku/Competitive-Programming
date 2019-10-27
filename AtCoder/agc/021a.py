N =  int(input())

if N < 10:
    print(N)
    exit()

def digitSum(n):
    return sum([int(a) for a in str(n)])

ans = max(digitSum(10**(len(str(N)) - 1) - 1) + int(str(N)[0]) - 1, digitSum(N))
print(ans)