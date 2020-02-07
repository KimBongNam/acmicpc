N, M, K = map(int, input().split())


if K >= 3:
    num = K // 3
    K = K % 3
    N -= num * 2
    M -= num

if K > 0:
    N -= K
team = 0
while N > 0 and M > 0:
    N -= 2
    M -= 1
    team += 1

if N < 0 or M < 0:
    team -= 1

print(team)