value = input()
sp_val = value.split()
int_val = [int(i) for i in sp_val]
fix_cost = int_val[0]
var_cost = int_val[1]
price = int_val[2]

ea = 0

total_cost = 0
total_rev = 0
if price < var_cost:
    print(-1)
else:
        
    while total_rev - total_cost <= 0:
        total_cost = fix_cost + var_cost * ea
        total_rev = price * ea
        ea+=1
    print(ea-1)