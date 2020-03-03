import sys

N, M = map(int, input().split())

A = 'WB' * (M//2)
B = 'BW' * (M//2)
if M%2 == 1: A += 'W'; B+= 'B'

lst = [sys.stdin.readline().strip() for _ in range(N)]
ans = []
for x in range(M-7):
    for y in range(N-7):
        lstcut = [_[x:x+8] for _ in lst[y:y+8]]
        sum_A = 0
        for i in range(8):
            for j in range(8):
                if i % 2 == 0:
                    if A[j] != lstcut[i][j]:
                        sum_A += 1
                else:
                    if B[j] != lstcut[i][j]:
                        sum_A += 1

        sum_B = 0
        for i in range(8):
            for j in range(8):
                if i % 2 == 0:
                    if B[j] != lstcut[i][j]:
                        sum_B += 1
                else:
                    if A[j] != lstcut[i][j]:
                        sum_B += 1
        ans.append(sum_A)
        ans.append(sum_B)
print(min(ans))
                


'''
sum_A = 0
for i in range(N):
    for j in range(M):
        if i % 2 == 0:
            if A[j] != lstcut[i][j]:
                sum_A += 1
        else:
            if B[j] != lstcut[i][j]:
                sum_A += 1

sum_B = 0
for i in range(N):
    for j in range(M):
        if i % 2 == 0:
            if B[j] != lstcut[i][j]:
                sum_B += 1
        else:
            if A[j] != lstcut[i][j]:
                sum_B += 1
print(min(sum_A, sum_B))
'''