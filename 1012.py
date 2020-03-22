import sys

sys.setrecursionlimit(1000000)
def DFS_visit(adj, u, visited):
    visited.append(u)
    for v in adj[u]:
        if v not in visited:
            DFS_visit(adj, v, visited)
 
 
def DFS(adj, s):
    visited =[]
    DFS_visit(adj, s, visited)
    return visited
 

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    dic = {i : [] for i in range(K)}
    lst = []
    for i in range(K):
        x, y = map(int, sys.stdin.readline().split())
        lst.append([x,y])
        for j in range(len(lst)):
            if [x-1,y] == lst[j] or [x,y-1] == lst[j] or [x+1,y]==lst[j] or [x,y+1]==lst:
                dic[i].append(j)
                dic[j].append(i)
    ans = []
    visited = []
    for i in range(K):
        if i in visited:
            continue
        a = DFS(dic,i)
        visited += a
        if set(a) not in ans:
            ans.append(set(a))
    print(len(ans))