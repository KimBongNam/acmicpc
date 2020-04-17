import sys
N = int(input())
lst = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
maxi = max(lst, key=lambda x : x[0])[0]
day = {i : 0 for i in range(1, maxi+1)}
lst.sort(key=lambda x: x[1])
for _ in range(N):
    d, w = lst.pop()
    while d != 0:
        if not day.get(d):
            day[d] = w
            break
        else:
            d -= 1
print(sum(day.values()))