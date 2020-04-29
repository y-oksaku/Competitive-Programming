def sol():
    S = input()

    if S[0] != 'A':
        print('WA')
        return

    if S[2: -1].count('C') != 1:
        print('WA')
        return

    for s in S[2:-1]:
        if s != 'C' and s.isupper():
            print('WA')
            return

    if S[1].isupper() or S[-1].isupper():
        print('WA')
        return

    print('AC')

sol()