import sys
N = int(input())
dic = {i+1:set() for i in range(N)}

def dfs(start):


for i in range(N-1):
    a, b= map(int, sys.stdin.readline().split())
    dic[a].add(b)
    dic[b].add(a)

for i in range(N):
    dic[i+1] = list(dic[i+1])

