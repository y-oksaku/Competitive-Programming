from collections import deque

W, H = map(int, input().split())
M = [list(map(int, input().split())) for _ in range(H)]

depth = [[-1] * W for _ in range(H)]

for stH in range(H):
    for stW in range(W):
        if depth[stH][stW] >= 0:
            continue

        now = M[stH][stW]
        st = deque([(stH, stW, 0)])
        while st:
            nh, nw, d = st.pop()

            if depth[nh][nw] >= 0:
                if abs(depth[nh][nw] - d) >= 3:
                    print('possible')
                    exit()
                continue
            depth[nh][nw] = d

            for h in [nh - 1, nh + 1]:
                if 0 <= h < H and M[h][nw] == now:
                    st.append((h, nw, d + 1))
            for w in [nw - 1, nw + 1]:
                if 0 <= w < W and M[nh][w] == now:
                    st.append((nh, w, d + 1))

print('impossible')