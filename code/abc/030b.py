N, M = map(int, input().split())
N %= 12

angM = M * 6
angN = (N / 12) * 360 + (M / 60) * 30
diff = abs(angM - angN)

print(min(diff, 360 - diff))