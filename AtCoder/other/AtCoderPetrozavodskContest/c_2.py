N = int(input())

def read(i):
    print(i, flush=True)
    s = input()
    if s == 'Vacant':
        exit()
    return s

s = read(0)
isMale = 0 if s == 'Male' else 1
s = read(N - 1)

A = [i % 2 == isMale for i in range(N)]

ok = 0
ng = N
while ng - ok > 1:
    mid = (ok + ng) // 2
    s = read(mid)

    isMale = s == 'Male'

    if isMale == A[mid]:
        ok = mid
    else:
        ng = mid

read(ng)
read(ok)
exit()
