import sys
sys.setrecursionlimit(1000000)
A, B, C = map(int, input().split())
21474 2147480 2147
def pro(A,B):
    print(A,B)
    if B == 0:
        return 1
    elif B % 2 == 0:
        return pro(A,B//2) ** 2
    elif B % 2 == 1:
        return (pro(A, B//2) ** 2 ) * A

ans = pro(A, B)
print(ans%C)