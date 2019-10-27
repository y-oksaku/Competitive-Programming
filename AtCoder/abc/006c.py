def sol():
    N, M = map(int, input().split())

    if M == 1:
        print('-1 -1 -1')
        return

    if M % 2 == 1:
        elder = 1
    else:
        elder = 0

    baby = (M - 3 * elder) // 4
    man = ((M - 3 * elder) % 4) // 2

    if elder + baby + man > N:
        print('-1 -1 -1')
        return

    R = N - man - baby - elder
    man += 2 * R
    baby -= R

    if baby >= 0:
        print('{} {} {}'.format(man, elder, baby))
        return

    print('-1 -1 -1')

sol()