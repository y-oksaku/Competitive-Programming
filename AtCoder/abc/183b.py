Sx, Sy, Gx, Gy = map(int, input().split())
Gy = -Gy

if Sx == Gx:
    print(Sx)
    exit()

a = (Gy - Sy) / (Gx - Sx)
print(-Sy / a + Sx)
