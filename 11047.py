import sys

N, K = map(int, input().split())
coin_list = [int(sys.stdin.readline()) for _ in range(N)]

cnt = 0
sum = 0
coin_list.reverse()
for i in coin_list:
    if sum + i <=K:
        cnt += (K-sum)//i
        sum += i * ((K-sum)//i)
    if sum == K:
        break
print(cnt)