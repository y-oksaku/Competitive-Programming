from heapq import heappush, heappop, heapify

N, sen, gosen, man = map(int, input().split())
A = list(map(lambda a: -int(a), input().split()))

heapify(A)
while A and man > 0:
    a = -heappop(A)
    c = max(1, min(man, a // 10000))
    a -= c * 10000
    man -= c
    if a >= 0:
        heappush(A, -a)

while A and gosen > 0:
    a = -heappop(A)
    c = max(1, min(gosen, a // 5000))
    a -= c * 5000
    gosen -= c
    if a >= 0:
        heappush(A, -a)

A = [-a for a in A]

cnt = 0
for a in A:
    c = -(-a // 1000)
    if c * 1000 == a:
        c += 1
    cnt += c

print('Yes' if cnt <= sen else 'No')
