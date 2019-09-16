import sys

n = int(sys.stdin.readline())
height = []
weight = []
for i in range(n):
    inp = sys.stdin.readline()
    inform = list(map(int,inp.split()))
    weight.append(inform[0])
    height.append(inform[1])

lst = []
for j in range(n):
    num = 0
    for k in range(n):
        if height[j] < height[k] and weight[j] < weight[k]:
            num += 1
    lst.append(num)
for p in lst:
    print(p+1, end = " ")