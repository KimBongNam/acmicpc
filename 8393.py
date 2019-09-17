import sys

inp = int(sys.stdin.readline().split()[0])
sum = 0
for i in range(1,inp+1):
    sum += i
print(sum)