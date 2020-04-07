import sys

N, M = map(int, input().split())
7 5
adj = [[0] * (N) for _ in range(N)]

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    adj[a][b] = 1
    adj[b][a] = 1

visited = set([0])
queue = []
for i in range(N):
    if adj[0][i] == 1:
        queue.append(i)

while queue:
    a = queue.pop()
    for i in range(N):
        if adj[a][i] == 1 and i not in visited:
            visited.add(i)
            queue.append(i)
print(1 if len(visited) == N else 0)