N = int(input())
ans = [0] * N
for a in map(int, input().split()):
    ans[a - 1] += 1
print(*ans, sep='\n')
