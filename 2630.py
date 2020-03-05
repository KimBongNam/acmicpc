import sys
N = int(input())


lst = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

ans =[0,0]
def check(lsts):
    ch = [all(k) for k in [[lsts[0][0] == j for j in i] for i in lsts]]
    if all(ch):
        if lsts[0][0] == 0:
            ans[0] += 1
        elif lsts[0][0] == 1:
            ans[1] += 1
    else:
        point = len(lsts)//2
        front = lsts[:point]
        rear = lsts[point:]
        check([i[point:] for i in front])
        check([i[point:] for i in rear])
        check([i[:point] for i in front])
        check([i[:point] for i in rear])

check(lst)
print(ans[0])
print(ans[1])
    