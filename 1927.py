import sys
import heapq
N = int(input())

lst = []
val = [int(sys.stdin.readline()) for _ in range(N)]

for i in val:
    if i==0:
        print(0 if len(lst)==0 else heapq.heappop(lst))
    else:
        heapq.heappush(lst, i)