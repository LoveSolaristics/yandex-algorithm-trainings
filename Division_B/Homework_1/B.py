N, i, j = map(int, input().split())

if abs(i - j) <= N - abs(i - j):
    print(abs(i - j) - 1)
else:
    print(N - abs(i - j) - 1)
