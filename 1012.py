import sys

def dfs(pos, unvisited):
    if lst[pos[1]+1][pos[0]] == 1:
        pos = [pos[0], pos[1]+1]
        unvisited.remove(pos)
        return dfs(pos, unvisited)
    elif lst[pos[1]][pos[0]+1] == 1:
        pos = [pos[0]+1,pos[1]]
        unvisited.remove(pos)
        return dfs(pos, unvisited)
    else:
        return pos, unvisited

T = int(input())
for i in range(T):
    M, N, K = map(int, input().split())
    lst = [[0]*(M+1) for _ in range(N+1)]
    for j in range(K):
        x, y = map(int, sys.stdin.readline().split())
        lst[y][x] = 1
    unvisited = []
    unvisited.append([x,y])
    cnt = 0
    while unvisited:
        pos = unvisited[0]
        pos, unvisited = dfs(pos, unvisited)
        cnt += 1
    print(cnt)