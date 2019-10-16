import sys

def binary_search(lst):
    if len(lst) <= 1:
        return lst
    else:
        a = []
        b = lst[len(lst)//2]
        c = []
        for i in lst:
            if i < b:
                a.append(i)
            elif i > b:
                c.append(i)
        return binary_search(a) +[b] + binary_search(c)


inp = list(map(int,sys.stdin.readlines()))
lsst = binary_search(inp[1:])
for i in lsst:
    print(i)