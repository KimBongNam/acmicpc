N = input()
lst = []
for i in N:
    lst.append(int(i))
if sum(lst) % 3 == 0 and 0 in lst:
    for i in reversed(sorted(lst)):
        print(i, end = '')
else:
    print(-1)