N, Y = map(int, input().split())

def find() :
    for yukichi in range(N+1) :
        if yukichi * 10000 > Y :
            break
        for higuchi in range(N+1-yukichi) :
            noguchi = N - yukichi - higuchi
            money = yukichi * 10000 + higuchi * 5000 + noguchi * 1000
            if money == Y :
                return (yukichi, higuchi, noguchi)
            if money > Y :
                break
    return (-1, -1, -1)

ans = find()

print('{} {} {}'.format(ans[0], ans[1], ans[2]))