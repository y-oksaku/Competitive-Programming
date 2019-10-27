def sol():
    Ax, Ay, Bx, By, Cx, Cy = map(int, input().split())

    S = abs((Bx - Ax) * (Cy - Ay) - (By - Ay) * (Cx - Ax))
    print(S / 2)


sol()