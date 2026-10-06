t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    rem_odd = n - (k - 1)
    if rem_odd > 0 and rem_odd % 2 != 0:
        print("YES")
        for _ in range(k - 1):
            print(1, end=" ")
        print(rem_odd)
        continue
        
    
    rem_even = n - 2 * (k - 1)
    if rem_even > 0 and rem_even % 2 == 0:
        print("YES")
        for _ in range(k - 1):
            print(2, end=" ")
        print(rem_even)
        continue
        
    print("NO")
