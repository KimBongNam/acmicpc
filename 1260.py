import sys


def dfs(admat, start, lst):
    lst.append(start)
    for j in range(1,node+1):
        if admat[start][j] == 1 and j not in lst:
            lst = dfs(admat,j,lst)
    return lst

def bfs(admat,start,node):
    lst = []
    
    lst.append(start)
    for i in range(1,node+1):
        for j in range(1,node+1):
            if admat[start][j] == 1 and j not in lst:
                lst.append(j)
        start = lst[i-1]
    print(*lst)

node, edge, start = map(int,input().split())
admat = [[0]*(node+1) for i in range(node+1)]


ls = sys.stdin.readlines()
lst = []
for i in ls:
    lst.append(list(map(int,i.split())))

for i in range(edge):
    admat[lst[i][0]][lst[i][1]] = 1
    admat[lst[i][1]][lst[i][0]] = 1

print(*dfs(admat,start, []))
bfs(admat,start, node)
