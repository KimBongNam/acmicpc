import sys
 
N, M = map(int, input().split())
11 10
r, c, d = map(int, input().split())
7 4 0
left = {0: [0,-1],
        1: [-1,0],
        2: [0,1],
        3: [1,0]}
front = {0: [-1,0],
        1: [0,1],
        2: [1,0],
        3: [0,-1]}
dlst = [0,1,2,3]
dxlst = [0,0,-1,1]
dylst = [1,-1,0,0]
lst = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
1 1 1 1 1 1 1 1 1 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 1 1 1 1 0 1
1 0 0 1 1 0 0 0 0 1
1 0 1 1 0 0 0 0 0 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 0 0 0 1 0 1
1 0 0 0 0 0 1 1 0 1
1 0 0 0 0 0 1 1 0 1
1 0 0 0 0 0 0 0 0 1
1 1 1 1 1 1 1 1 1 1

cnt = 0

while True:
    
    if lst[r][c] == 0:
        lst[r][c] = -1
        cnt += 1
    
    dr, dc = left[d]
    available = False
    for i in range(4):
        if lst[r+dxlst[i]][c+dylst[i]] == 0:
            available = True
    
    if not available:
        d = dlst[(d+1)%4]
        dr, dc = front[d]
        r, c = r-dr, c-dc
        if lst[r][c] == 1:
            break

        else:
            continue

    if lst[r+dr][c+dc] == 0:
        print(d)
        d = dlst[d-1]
        dr, dc = front[d]
        r, c = r+dr, c+dc
        continue
    
    else:
        d = dlst[d-1]
    
print (cnt)