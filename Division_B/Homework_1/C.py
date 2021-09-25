x, y, z = map(int, input().split())

a = [i for i in range(1, 13)]

if (x in a) and (y in a) and (x != y):
    print(0)
else:
    print(1)