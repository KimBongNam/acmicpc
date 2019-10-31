arrangement = input()
a = True
    
answer = 0
while a:
    origin = arrangement
    if arrangement[0] == "(" and arrangement[1] ==")":
        arrangement = arrangement[2:]
           
    if arrangement[-1]==")" and arrangement[-2] == "(":
        arrangement = arrangement[:-2]
        
    if origin == arrangement:
        a = False
stack = []
for i,sig in enumerate(arrangement):
    if sig == '(':
        stack.append(i)
    else:
        del stack[-1]
        if arrangement[i-1]=="(":
            answer += len(stack)
        else:
            answer += 1
            
print(answer)