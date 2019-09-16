n = input()
num = 1
if len(n)==1:
    compare = n+n
    n = "0"+n
else:
    compare = n[-1]+str(int(n[0])+int(n[1]))[-1] 
while n != compare:
    compare = compare[-1]+str((int(compare[0]) + int(compare[-1])))[-1]
    num += 1
print(num)