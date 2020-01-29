import sys
N, C = map(int, input().split())
lst = [int(sys.stdin.readline()) for _ in range(N)]
lst.sort()
low = 1
high = lst[-1] - lst[0]
ans = 0
while low <= high:
    mid = (low + high) // 2
    current = lst[0]
    cnt = 1
    for i in range(1,N):
        if lst[i]-current >= mid:
            current = lst[i]
            cnt += 1
    if cnt >= C:
        if ans < mid:
            ans = mid
        low = mid + 1
    elif cnt < C:
        high = mid - 1
print(ans)