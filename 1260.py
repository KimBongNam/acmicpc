import sys


def dfs(admat, start, node):
    lst = []
    lst.append(start)
    or_start=start
    for i in range(1,node+1):
        for j in range(1,node+1):
            if admat[start][j] == 1 and j not in lst:
                lst.append(j)
                start = j
                break
        
            if j == node:
                start = or_start
    print(*lst)

def bfs(admat,start,node):
    lst = []

    lst.append(start)
    while len(lst) != node:
        for i in range(1,node+1):
            if admat[start][i] == 1:
                lst.append(i)

node, edge, start = map(int,input().split())
admat = [[0]*(node+1) for i in range(node+1)]


ls = sys.stdin.readlines()
lst = []
for i in ls:
    lst.append(list(map(int,i.split())))

for i in range(edge):
    admat[lst[i][0]][lst[i][1]] = 1
    admat[lst[i][1]][lst[i][0]] = 1
dfs(admat,start, node)
