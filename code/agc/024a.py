A, B, C, K = map(int, input().split())

ans = (-1)**(K % 2) * (A - B)
print(ans)