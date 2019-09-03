S = input()

sToI = {
    'O' : '0',
    'D' : '0',
    'I' : '1',
    'Z' : '2',
    'S' : '5',
    'B' : '8',
}

S = S.translate(str.maketrans(sToI))
print(S)