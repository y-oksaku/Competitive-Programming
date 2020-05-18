import string
N = int(input())
alph = string.ascii_lowercase

ans = []
A = [0]
def search():
    if len(A) == N:
        ans.append(tuple(A))
        return

    mx = max(A)
    for i in range(mx + 2):
        A.append(i)
        search()
        A.pop()
    return

search()

for a in ans:
    print(''.join(alph[i] for i in a))
