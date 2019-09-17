import sys

inp = sys.stdin.readline()
letters = inp.split()[0]

num = 0
for i in letters:
    print(i, end='')
    
    if num ==9:
        print()
        num = 0
        continue
    num+=1