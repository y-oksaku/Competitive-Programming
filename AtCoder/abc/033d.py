from math import atan2, pi

def sol():
    N = int(input())
    points = [tuple(map(int, input().split())) for _ in range(N)]
    EPS = 1e-12

    obtuseTri = 0
    rightTri = 0

    for i, (x, y) in enumerate(points):
        angles = []
        for j, (u, v) in enumerate(points):
            if i == j:
                continue
            angles.append(atan2(u - x, v - y))

        angles.sort()
        angles += [a + 2 * pi for a in angles]

        rightAngle = []
        right = 1
        for left in range(N - 1):
            while right < len(angles) and angles[right] - angles[left] < pi / 2 + EPS:
                right += 1
            rightAngle.append(right)

        banishAngle = []
        right = 1
        for left in range(N - 1):
            while right < len(angles) and angles[right] - angles[left] < pi:
                right += 1
            banishAngle.append(right)

        for j, (a, b) in enumerate(zip(rightAngle, banishAngle)):
            obtuseTri += b - a
            diff = angles[a - 1] - angles[j]
            if abs(diff - pi / 2) < EPS:
                rightTri += 1

    allTri = N * (N - 1) * (N - 2) // 6
    print(allTri - rightTri - obtuseTri, rightTri, obtuseTri)

sol()