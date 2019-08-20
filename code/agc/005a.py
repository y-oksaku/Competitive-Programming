def sol():
    X = input()

    scount = 0
    ans = 0
    for x in X:
        if x == 'S':
            scount += 1
        else:
            if scount == 0:
                ans += 1
            else:
                scount -= 1

    print(ans * 2)

sol()