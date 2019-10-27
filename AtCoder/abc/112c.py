N = int(input())
axis = []

for i in range(N) :
    x, y, h = map(int, input().split())
    axis.append((x, y, h))

def sol() :
    for cx in range(0, 101) :
        for cy in range(0, 101) :
            axis.sort(key = lambda A : abs(A[0] - cx) + abs(A[1] - cy))
            H = axis[0][2] + abs(axis[0][0] - cx) + abs(axis[0][1] - cy)
            for x, y, h in axis :
                if not h == max(H - abs(x - cx) - abs(y - cy), 0) :
                    break
            else :
                return (cx, cy, H)
    return (-1, -1, -1)

cx, cy, H = sol()
if cx == -1 :
    print('-1')
else :
    print('{} {} {}'.format(cx, cy, H))
