T = int(input())
for i in range(T):
    H, W, N = map(int, input().split())
    A, B = divmod(N, H)
    if B == 0:
        print(H * 100 + A)
    else:
        print(B*100 + A+1)