num = int(input())
test = input()
lst = test.split()
in_lst = [int(i) for i in lst]
x = in_lst[0]
y = in_lst[1]
num = in_lst[2]
locate = []
for i in range(num):
    xy = input()
    a = xy.split()
    b = [int(i) for i in a]
    locate.append(b)
    for i in locate[:-1]:
        locate[-1][0]