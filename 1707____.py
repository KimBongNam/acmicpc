import sys
def dfs(num, visited,a , b,p):
    for i in graph[num]:
        if i not in visited:
            if p == 1:
                visited.append(i)
                a.add(i)
                dfs(i, visited,a ,b,0)
            else:
                visited.append(i)
                b.add(i)
                dfs(i,visited,a,b,1)


def dfsall(node, visited):
    a = set()
    b = set()
    for k in range(1,node+1):
        if k not in visited:
            dfs(k, visited, a, b,0)
    return a,b


num = int(input())

for i in range(num):
    nodes, edges = map(int, input().split())
    graph = [[] for _ in range(nodes+1)]
    for j in range(edges):
        x,y = map(int, sys.stdin.readline().split())
        graph[x].append(y)
        graph[y].append(x)
    a,b = dfsall(nodes,[])

    print("YES" if len(a&b)==0 else "NO")
    


    
    