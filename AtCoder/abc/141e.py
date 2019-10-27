from collections import deque

N = int(input())
S = input()

def isOk(leng):
    strList = set()
    que = deque([])
    for left in range(N - leng + 1):
        sub = S[left: left + leng]
        if sub in strList:
            return True
        que.append(sub)
        if len(que) >= leng:
            strList.add(que.popleft())
    return False

ok = 0
ng = N

while ng - ok > 1:
    mid = (ng + ok) // 2
    if isOk(mid):
        ok = mid
    else:
        ng = mid

print(ok)