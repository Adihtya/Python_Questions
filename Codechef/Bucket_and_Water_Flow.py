T = int(input())
for i in range(T):
    W, X, Y, Z = map(int, input().split())
    total_water = W + (Y * Z)
    if total_water < X:
        print("unfilled")
    elif total_water == X:
        print("filled")
    else:
        print("overflow")
