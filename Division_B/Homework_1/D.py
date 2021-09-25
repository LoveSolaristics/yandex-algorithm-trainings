n = int(input())

a = list(map(int, input().split()))

if n % 2 == 0:
    print(a[n // 2])
else:
    print(a[(n - 1) // 2])