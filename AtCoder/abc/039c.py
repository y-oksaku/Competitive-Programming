S = input()
N = len(S)

piano = 'WBWBWWBWBWBWWBWBWWBWBWBWWBWBWWBWBWBWWBWBWWBWBWBWWBWBWWBWBWBWWBWBWWBWBWBW'
ans = ['Do', 'Do#', 'Re', 'Re#', 'Mi', 'Fa', 'Fa#', 'So', 'So#', 'La', 'La#', 'Si']

for i in range(len(piano)):
    for j, (s, t) in enumerate(zip(piano[i:i + N], S)):
        if s != t:
            break
    else:
        print(ans[i % 12])
        break
