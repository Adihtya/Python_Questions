t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    min_ops = float("inf")
    
    for num in a:
        ops = 0
        while num % 2 == 0:
            num //= 2
            ops += 1
            
        if ops < min_ops:
            min_ops = ops
            
        if min_ops == 0:
            break
            
    print(min_ops)
