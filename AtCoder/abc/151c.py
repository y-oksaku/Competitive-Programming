from collections import defaultdict

N, M = map(int, input().split())

results = defaultdict(list)
for _ in range(M):
    p, s = input().split()
    results[p].append(s)

acCnt = 0
waCnt = 0
for result in results.values():
    cnt = 0
    for s in result:
        if s == 'AC':
            acCnt += 1
            break
        cnt += 1
    else:
        continue
    waCnt += cnt

print(acCnt, waCnt)