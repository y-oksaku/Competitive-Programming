A, B, C, D, E = map(int, input().split())

numList = [
    A + B + C,
    A + B + D,
    A + B + E,
    A + C + D,
    A + C + E,
    A + D + E,
    B + C + D,
    B + C + E,
    B + D + E,
    C + D + E,
]

numList.sort(reverse=True)
print(numList[2])