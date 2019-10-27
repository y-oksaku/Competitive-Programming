from collections import defaultdict

def sol():
    H, W, N = map(int, input().split())
    origin = defaultdict(int)

    ans = [0 for _ in range(10)]
    ans[0] = (H - 2) * (W - 2)

    def addBlack(h, w):
        ans[origin[(h, w)]] -= 1
        ans[origin[(h, w)] + 1] += 1
        origin[(h, w)] += 1

    for _ in range(N):
        h, w = map(int, input().split())

        for a in [-1, 0, 1]:
            for b in [-1, 0, 1]:
                if 2 <= h + a <= H - 1 and 2 <= w + b <= W - 1:
                    addBlack(h + a, w + b)

    for a in ans:
        print(a)

sol()