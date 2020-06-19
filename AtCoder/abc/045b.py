S = {
    'a': list(input()[::-1]),
    'b': list(input()[::-1]),
    'c': list(input()[::-1]),
}

s = 'a'
while True:
    if not S[s]:
        print(s.upper())
        exit()
    s = S[s].pop()
