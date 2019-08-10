num = int(input())
in_val = input()
arr = in_val.split(" ")
int_arr = []
for i in arr:
    int_arr.append(int(i))
int_arr.sort()
print(int_arr[0],int_arr[num-1])