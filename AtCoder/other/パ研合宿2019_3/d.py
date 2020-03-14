N = int(input())
A = [input() for _ in range(5)]
iToS = ['R', 'B', 'W']

def count(col):
    ret = {'R': 0, 'B': 0, 'W': 0, '#': 0}

    for i in range(5):
        ret[A[i][col]] += 1

    return ret

dp = [0] * 3

for col in range(N):
    newDp = [0] * 3
    cnt = count(col)
    for i, s in enumerate(iToS):
        diff = 5 - cnt[s]
        newDp[i] = diff + min([dp[(i + j) % 3] for j in range(1, 3)])
    dp = newDp

print(min(dp))
