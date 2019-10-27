T = int(input())

ans = []
for _ in range(T):
    N = int(input())
    D = list(map(int, list(input())))

    for middle in range(10):
        S = []
        one = -1
        two = -1
        for d in D:
            if d < middle:
                if one > d:
                    break
                one = d
                S.append('1')
            elif d > middle:
                if two > d:
                    break
                two = d
                S.append('2')
            else:
                if two <= d:
                    two = d
                    S.append('2')
                else:
                    one = d
                    S.append('1')
        else:
            ans.append(''.join(S))
            break
    else:
        ans.append('-')

print(*ans, sep='\n')