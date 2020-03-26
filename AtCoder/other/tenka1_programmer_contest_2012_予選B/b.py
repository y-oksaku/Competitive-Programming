import string
S = input()
Alph = string.ascii_uppercase
alph = string.ascii_lowercase

B = set(alph)
lowerToUpper = {a: A for a, A in zip(alph, Alph)}
upperToLower = {A: '_' + a for a, A in zip(alph, Alph)}

def sol(S):
    head = ''
    while S != '' and S[0] == '_':
        S = S[1:]
        head += '_'

    tail = ''
    while S != '' and S[-1] == '_':
        S = S[:-1]
        tail += '_'

    if len(S) <= 1:
        return head + S + tail

    if S.count('__') > 0:
        return head + S + tail

    if S.count('_') > 0 and sum([S.count(a) for a in Alph]) > 0:
        return head + S + tail

    if S.count('_'):
        words = S.split('_')
        T = ''
        for i, word in enumerate(words):
            if not word[0] in B:
                return head + S + tail
            if i == 0:
                T += word
                continue
            T += lowerToUpper[word[0]] + word[1:]
        return head + T + tail

    if not S[0] in B:
        return head + S + tail

    for fr, to in upperToLower.items():
        S = S.replace(fr, to)
    return head + S + tail

print(sol(S))
