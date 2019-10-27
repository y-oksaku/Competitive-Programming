Y, M, D = map(int, input().split('/'))

def isUru(year):
    if Y % 400 == 0:
        return True
    elif Y % 100 == 0:
        return False
    elif Y % 4 == 0:
        return True
    else:
        return False

dayOfMonth = {
    1 : 31,
    2 : 28 if not isUru(Y) else 29,
    3 : 31,
    4 : 30,
    5 : 31,
    6 : 30,
    7 : 31,
    8 : 31,
    9 : 30,
    10 : 31,
    11 : 30,
    12 : 31,
}

for _ in range(400):  # 1月1日は必ずOKなので
    if Y % (M * D) == 0:
        print('{}/{:02}/{:02}'.format(Y, M, D))
        break
    D += 1
    if D > dayOfMonth[M]:
        D = 1
        M += 1
        if M >= 13:
            Y += 1
            M = 1

