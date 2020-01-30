import sys
N = int(input())
lst = [list(map(int, sys.stdin.readline().split())) for i in range(N)]
dic = {1:0, 2:0, 3:0}
def check(lst):
    element = lst[0]
    for i in lst:
        if i != element:
            return False
    dic[element] += 1
    return True

def resize(lst):
    size = len(lst)/3
    a = []
    for i in range(size):
        a += lst[i:3*i-1]

while not check(lst):
    