Q, L = map(int, input().split())
st = []
cnt = 0

ans = []
isRunning = True

for _ in range(Q):
    query = tuple(input().split())

    if not isRunning:
        continue

    if len(query) == 1:
        if query[0][0] == 'T':
            if cnt == 0:
                ans.append('EMPTY')
                isRunning = False
                continue
            ans.append(st[-1][0])
        else:
            ans.append(cnt)
        continue

    if len(query) == 2:
        N = int(query[1])
        if N > cnt:
            ans.append('EMPTY')
            isRunning = False
            continue
        cnt -= N
        while N > 0:
            m, n = st.pop()
            N -= n
            if N < 0:
                st.append((m, -N))
        continue

    N, M = int(query[1]), int(query[2])
    st.append((M, N))
    cnt += N
    if cnt > L:
        ans.append('FULL')
        isRunning = False
        continue

if len(ans) > 0:
    print(*ans, sep='\n')
if isRunning:
    print('SAFE')
