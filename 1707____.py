import sys

num = int(input())

for i in range(num):
    nodes, edges = map(int, input().split())
    graph = {n : [] for n in range(1, nodes+1)}
    for j in range(edges):
        x, y = map(int, sys.stdin.readlines().split())
        graph[x].append(y)
        graph[y].append(x)
    
    
    