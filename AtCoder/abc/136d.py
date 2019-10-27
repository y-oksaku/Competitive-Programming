S = input()
N = len(S)

ans = [0] * N
dist = [0] * N

def ceil(x, y) :
    return (x + y - 1) // y

nowIndex = 0
while nowIndex < N :
    leftL = nowIndex
    while leftL < N and S[leftL] == 'R' :
        leftL += 1
    nextR = leftL
    while nextR < N and S[nextR] == 'L' :
        nextR += 1
    ans[leftL - 1] = ceil(leftL - nowIndex, 2) + (nextR - leftL) // 2
    ans[leftL] = nextR - nowIndex - ans[leftL - 1]
    nowIndex = nextR

print(*ans)