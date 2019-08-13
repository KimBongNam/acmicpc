f_num = [0,1]
num = int(input())
for i in range(num -1):
    f_num.append(f_num[-1]+f_num[-2])
print(f_num[num])