import sys

inp = sys.stdin.readline()
num = int(inp)
answer = 0
for i in range(num):
    sum = i
    for j in (str(i)):
        sum += int(j)
    if sum == num:
        answer = i
        break
print(answer)