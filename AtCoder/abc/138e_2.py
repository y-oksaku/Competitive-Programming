from bisect import bisect_left

S = input()
T = input()

if not set(list(T)) <= set(list(S)):
    print(-1)
    exit()

sToI = {s: [] for s in set(list(S))}
for i, s in enumerate(S):
    sToI[s].append(i)

now = 0
R = 0
for t in T:
    I = sToI[t]
    nx = bisect_left(I, now)

    if nx == len(I):
        nx = 0
        R += 1

    now = I[nx] + 1

print(now + R * len(S))
