N = int(input())
word = input().lower()

ans = [[]]

for w in word:
    if w == ' ':
        ans.append([])
    if w == 'b' or w == 'c':
        ans[-1].append('1')
    if w == 'd' or w == 'w':
        ans[-1].append('2')
    if w == 't' or w == 'j':
        ans[-1].append('3')
    if w == 'f' or w == 'q':
        ans[-1].append('4')
    if w == 'l' or w == 'v':
        ans[-1].append('5')
    if w == 's' or w == 'x':
        ans[-1].append('6')
    if w == 'p' or w == 'm':
        ans[-1].append('7')
    if w == 'h' or w == 'k':
        ans[-1].append('8')
    if w == 'n' or w == 'g':
        ans[-1].append('9')
    if w == 'z' or w == 'r':
        ans[-1].append('0')

res = []
for a in ans:
    if a:
        res.append(''.join(a))

print(*res)