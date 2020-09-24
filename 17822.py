import sys

def rotate(lst):
    lst.insert(0, lst[-1])
    del lst[-1]
    return lst

def etator(lst):
    lst.append(lst[0])
    del lst[0]
    return lst
dx = [0,0,1,-1]
dy = [1,-1,0,0]
N, M, T = map(int, input().split())
lst = []
for _ in range(N):
    lst.append(list(map(int, sys.stdin.readline().split())))

for _ in range(T):
    x, d, k = map(int, sys.stdin.readline().split())
    if d == 0:
        for i in range(N):
            lst[i] = rotate(lst[i])
        lst = rotate(lst)
    else:
        for i in range(N):
            lst[i] = etator(lst[i])
        lst = etator(lst)
    
    
