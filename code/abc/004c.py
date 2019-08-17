def sol():
    N = int(input())
    card = [str(i) for i in range(1, 7)]

    M = (N // 5) % 6
    card = card[M:] + card[:M]

    for i in range(N % 5):
        card[(i % 5)], card[(i % 5) + 1] = card[(i % 5) + 1], card[(i % 5)]

    print(''.join(card))


sol()