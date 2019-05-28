import re

S = input()
result = re.match(r'\A(dream|dreamer|erase|eraser)+\Z',S)

if result :
    print('YES')
else :
    print('NO')