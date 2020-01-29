N, M = map(int, input().split())
A_arr = list(map(int, input().split()))
B_arr = list(map(int, input().split()))

A_min = 0
B_min = 0

while A_min < N and B_min <M:
    if A_arr[A_min] < B_arr[B_min]:
        print(A_arr[A_min], end = ' ')
        A_min += 1
    else:
        print(B_arr[B_min], end = ' ')
        B_min += 1
if A_min == N:
    B_arr = B_arr[B_min:]
    for i in B_arr:
        print(i, end = ' ')
elif B_min == M:
    A_arr = A_arr[A_min:]
    for i in A_arr:
        print(i, end = ' ')