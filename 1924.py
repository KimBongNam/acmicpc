import sys

day = ["MON","TUE","WED","THU","FRI","SAT","SUN"]
mon = [31,28,31,30,31,30,31,31,30,31,30,31]
inp = sys.stdin.readline().split()
inp = list(map(int,inp))
date = 0
for i in range(1,inp[0]):
    date += mon[i-1]
date += inp[1]
print(day[date % 7 - 1])
