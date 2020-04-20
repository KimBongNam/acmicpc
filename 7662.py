import sys
import heapq

T = int(input())

for _ in range(T):
    Q = int(sys.stdin.readline().strip())
    lst = []
    for __ in range(Q):
        command = sys.stdin.readline().split()
        if command[0] == 'I':
            heapq.heappush(lst, int(command[1]))
        else:
            if len(lst) != 0:
                if command[1] == '-1':
                    heapq.heappop(lst)
                else:
                    lst.pop(lst.index(heapq.nlargest(1, lst)[0]))
    if len(lst)==0:
        print("EMPTY")
    else:
        print(heapq.nlargest(1,lst)[0], lst[0])
