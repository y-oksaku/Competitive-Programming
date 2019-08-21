N, K = map(int, input().split())
point = []
for _ in range(N) :
    x, y = map(int, input().split())
    point.append((x, y))

ans = float('inf')
for lx, _ in point :
    for rx, _ in point :
        if lx > rx :
            continue
        for _, ly in point :
            for _, ry in point :
                if ly > ry :
                    continue
                count = 0
                for x, y in point :
                    if lx <= x <= rx and ly <= y <= ry :
                        count += 1
                if count >= K :
                    ans = min(ans, (rx - lx) * (ry - ly))

print(ans)