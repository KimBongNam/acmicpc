first, num = map(int, input().split())
lst = [first]
while lst[-1] not in lst[:-1]:
    s = 0
    for i in str(lst[-1]):
        s += int(i)**num
    lst.append(s)

print(lst.index(lst[-1]))