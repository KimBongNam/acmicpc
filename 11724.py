import sys
sys.setrecursionlimit(10000)
nodes, edges = map(int,input().split())
admat = [[0]* (nodes+1) for i in range(nodes+1)]
inp = sys.stdin.readlines()
visited = [0 for i in range(nodes+1)]
for i in range(edges):
    x, y = map(int, inp[i].split())
    admat[x][y] = 1
    admat[y][x] = 1

def dfs(start):
    visited[start] = 1
    for i in range(1,nodes+1):
        if admat[start][i] == 1 and visited[i] == 0:
            dfs(i)

t = 0
for i in range(1,nodes+1):
    if visited[i] == 0:
        t += 1
        dfs(i)

print(t)