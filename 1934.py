T = int(input())
for i in range(T):
    A, B = map(int,input().split())
    gcd = 1
    for i in range(1, min(A,B)+1):
        if A%i == 0 and B%i==0:
            gcd = i
    lcm = (A * B)//gcd 

    print(lcm)
