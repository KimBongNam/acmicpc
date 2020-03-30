import sys
import heapq


T = int(input())
for _ in range(T):
    Q = int(input())
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
                    lst.pop()
                    heapq.heapify(lst)
        
    if len(lst)==0:
        print("EMPTY")
    else:
        print(max(lst), min(lst))