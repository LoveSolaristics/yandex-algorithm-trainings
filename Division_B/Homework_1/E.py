def distance(point1, point2):
    return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5


d = int(input())
x, y = map(int, input().split())

A = (0, 0)
B = (d, 0)
C = (0, d)

X = (x, y)

if (x >= 0) and (y >= 0) and (-x + d >= y):
    print(0)
else:
    AX = distance(A, X)
    BX = distance(B, X)
    CX = distance(C, X)

    if AX <= BX and AX <= CX:
        print(1)
    elif BX <= AX and BX <= CX:
        print(2)
    else:
        print(3)