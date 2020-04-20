import sys
N = int(input())
a, b, c = 0, 1, 2
for i in range(3,N+1):
    a, b, c = b, c, (b+c)%15746
if N == 1:
    print(1)
elif N == 2:
    print(2)
else:
    print(c)