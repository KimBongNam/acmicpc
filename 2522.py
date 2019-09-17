num = int(input())
for i in range(-num+1, num):
    q = abs(i)
    print(" "* q + "*"*(num-q))