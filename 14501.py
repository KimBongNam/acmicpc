import sys
N = int(input())
time = []
price = []
for _ in range(N):
    T, P = map(int, sys.stdin.readline().split())
    time.append(T)
    price.append(P)

