N = int(input())
lst = list(map(int, input().split()))
s = sorted(lst)

for i in range(N):
    s[N-1-i] 
cnt = 0
for i in range(N-1, 0, -1):
    for j in range(i):
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]
            cnt += 1

print(cnt)