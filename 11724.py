def dfs(admat, start, lst, sum):
    lst.append(start)
    print("!!!")
    for j in range(1,len(admat)):
        print("@@@")
        if admat[start][j] == 1 and j not in lst:
            sum += 1
            lst = dfs(admat,j,lst,sum)
            
    return sum

import sys

node, edge = map(int,input().split())
ad_mat = [[0]*(node+1) for i in range(node+1)]
inp = sys.stdin.readlines()
lst = []
for i in inp:
    lst.append(list(map(int,i.split())))

for i in range(edge):
    ad_mat[lst[i][0]][lst[i][1]] = 1
    ad_mat[lst[i][1]][lst[i][0]] = 1

print(dfs(ad_mat,1,[],0))
