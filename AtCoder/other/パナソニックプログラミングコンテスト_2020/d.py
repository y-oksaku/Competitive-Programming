import string

N = int(input())
alph = string.ascii_lowercase

def search(S, mx):
    if len(S) == N:
        yield S
    else:
        for s in alph[: mx]:
            for w in search(S + s, mx):
                yield w
        for w in search(S + alph[mx], mx + 1):
            yield w

ans = list(search('', 0))
print(*ans, sep='\n')
