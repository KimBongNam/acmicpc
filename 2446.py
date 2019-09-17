num = int(input())
for i in range(-num+1,num):
    i = abs(i)
    print(" "*(num-i-1) + "*"*(2*i+1))