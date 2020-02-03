import sys
N = int(input())
lst = [list(map(int, sys.stdin.readline().split())) for i in range(N)]
dic = {1:0, 2:0, 3:0}
def check(lst, dic):
    element = lst[0]
    if len(lst) == 1:
        dic[element] += 1
    else:
        p = True
        for i in lst:
            if i != element:
                p = False
                small = []
                size = len(lst)
                for row in range(0, size, size // 3):
                    for col in range(0, size, size // 3):
                        small = [x[col: col + size // 3] for x in lst[row: row + size //3]]
                        return check(small, dic)
        if p:
            dic[element] += 1

check(lst, dic)
for i in dic.values():
    print(i)