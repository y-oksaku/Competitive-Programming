N = int(input()) % 10

H = [2, 4, 5, 7, 9]
P = [0, 1, 6, 8]
B = [3]

if N in H:
    print('hon')
if N in P:
    print('pon')
if N in B:
    print('bon')
