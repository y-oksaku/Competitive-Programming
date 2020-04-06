H, W = map(int, input().split())
Z = [input() for _ in range(H)]
D = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (-1, 1), (1, 1), (1, -1)]

visited = [[False] * W for _ in range(H)]

def search(sh, sw):
    left = 10**18
    right = -1
    st = [(sh, sw)]
    visited[sh][sw] = True
    cnt = 0
    while st:
        h, w = st.pop()
        cnt += 1
        left = min(left, w)
        right = max(right, w)

        for dh, dw in D:
            if 0 <= h + dh < H and 0 <= w + dw < W and not visited[h + dh][w + dw] and Z[h + dh][w + dw] == 'o':
                st.append((h + dh, w + dw))
                visited[h + dh][w + dw] = True
    return (cnt, (right - left + 1) // 5)

A, B, C = 0, 0, 0
for h in range(H):
    for w in range(W):
        if Z[h][w] == 'o' and not visited[h][w]:
            cnt, scale = search(h, w)
            cnt //= scale**2
            if cnt == 12:
                A += 1
            elif cnt == 16:
                B += 1
            else:
                C += 1

print(A, B, C)
