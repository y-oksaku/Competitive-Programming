S = input()
cnt = 0

for s, t in zip(S, S[:: -1]):
    if s != t:
        cnt += 1

print(cnt // 2)