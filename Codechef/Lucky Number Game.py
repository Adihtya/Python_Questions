# cook your dish here
t = int(input())

for _ in range(t):
    n, a, b = map(int, input().split())
    arr = list(map(int, input().split()))

    bob_only = 0
    alice_only = 0
    common = 0

    for x in arr:
        if x % a == 0 and x % b == 0:
            common += 1
        elif x % a == 0:
            bob_only += 1
        elif x % b == 0:
            alice_only += 1

    if common > 0:
        if bob_only >= alice_only:
            print("BOB")
        else:
            print("ALICE")
    else:
        if bob_only > alice_only:
            print("BOB")
        else:
            print("ALICE")
