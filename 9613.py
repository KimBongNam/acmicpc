import sys

def G(A,B):
    if A<B: 
        A,B = B,A
    if A%B==0:
        return B
    return G(A%B,B)
t = int(input())
for i in range(t):
    lst = list(map(int, sys.stdin.readline().split()))
    n = lst[0]
    lst = lst[1:]
    sum = 0
    for i in range(n):
        for j in range(i+1, n):
            gcd = G(lst[i],lst[j])
            sum += gcd

    print(sum)
