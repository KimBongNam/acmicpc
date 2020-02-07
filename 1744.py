import sys

N = int(input())
minus = 0
plus = 0
zero = 0
minus_list = []
plus_list = []
new_plus = []

for i in range(N):
    num = int(sys.stdin.readline())
    if num == 1:
        new_plus.append(num)
    elif num > 0:
        plus += 1
        plus_list.append(num)
    elif num < 0:
        minus += 1
        minus_list.append(num)
    else:
        zero += 1

minus_list.sort()
plus_list.sort()
plus_list.reverse()

new_minus = []
i = 0
while minus >= 2:
    new_minus.append(minus_list[i] * minus_list[i+1])
    minus -= 2
    i += 2
if minus == 1 and zero != 0:
    minus -= 1
    zero -= 1
elif minus == 1 and zero == 0:
    new_minus.append(minus_list[-1])

i = 0
while plus >= 2:
    new_plus.append(plus_list[i] * plus_list[i+1])
    plus -= 2
    i += 2
if plus == 1:
    new_plus.append(plus_list[-1])
print(plus_list,minus_list,new_minus,new_plus)
print(sum(new_plus) + sum(new_minus))