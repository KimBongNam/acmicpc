import sys
K = int(input())

for _ in range(K):
    V, E = map(int, input().split())
    adj = [[0]*(V+1) for _ in range(V+1)]
    for __ in range(E):
        a, b = map(int, sys.stdin.readline().split())
        adj[a][b] = 1
        adj[b][a] = 1
    

    visited_a = set([1])
    visited_b = set()
    queue = []
    for i in range(1,V+1):
        if adj[1][i] == 1:
            queue.append(i)
            visited_b.add(i)
    a = 1
    while queue:
        start = a
        a = queue.pop()
        for i in range(1, V+1):
            if adj[a][i] == 1 and i != start:
                if start in visited_a:
                    visited_b.add(i)
                elif start in visited_b:
                    visited_a.add(i)
                queue.append(i)
            if len(visited_a) + len(visited_b) != len(visited_a.union(visited_b)):
                break
    if len(visited_a) + len(visited_b) != len(visited_a.union(visited_b)):
        print("NO")
    else:
        print("YES")
