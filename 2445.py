num = int(input())
lst = [("*"*(i+1) + " "*(2*(num-1-i)) + "*"*(i+1)) for i in range(num)]
for j in range(num):
    print(lst[j])
for l in range(num-1):
    print(lst[num-l-2])

