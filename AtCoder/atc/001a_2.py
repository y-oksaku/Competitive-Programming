from collections import deque

H, W = map(int, input().split())
chart = [input() for _ in range(H)]

start = None
end = None
for h, line in enumerate(chart):
    for w, s in enumerate(line):
        if s == 's':
            start = (h, w)
        if s == 'g':
            end = (h, w)

que = deque([start])
visited = [[False] * W for _ in range(H)]
while que:
    nh, nw = que.popleft()
    if visited[nh][nw]:
        continue
    visited[nh][nw] = True

    for h in [nh - 1, nh + 1]:
        if 0 <= h < H and (chart[h][nw] == '.' or chart[h][nw] == 's' or chart[h][nw] == 'g'):
            que.append((h, nw))
    for w in [nw - 1, nw + 1]:
        if 0 <= w < W and (chart[nh][w] == '.' or chart[nh][w] == 's' or chart[nh][w] == 'g'):
            que.append((nh, w))

print('Yes' if visited[end[0]][end[1]] else 'No')