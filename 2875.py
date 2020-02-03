N, M, K = map(int, input().split())


team = 0
while N * M != 0:
    N -= 2
    M -= 1
    team += 1
outlier = N + M

outlier -= K

team -= abs(outlier / 3)
team = int(team)
print(team)