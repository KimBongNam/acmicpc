import sys

inp = sys.stdin.readlines()
num = inp[1].split()
sum = 0
for i in num[0]:
    sum += int(i)
print(sum)