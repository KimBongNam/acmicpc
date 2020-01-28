import sys

num = int(input())
for i in range(num):
    vol = int(sys.stdin.readline())
    num = [i for i in range(1, vol+1)]
    inp = list(map(int, input().split()))
    visited = [0] * (vol+1)
    cnt = 0
    for j in range(1,vol+1):
        if visited[j] == 0:
            visited[j] = 1
            search = inp[j-1]
            while visited[search] == 0:
                visited[search] = 1
                search = inp[search-1]
            cnt += 1
    print(cnt)

    