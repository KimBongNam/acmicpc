from string import ascii_uppercase
class Stack:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)

SS=Stack()
org= input()
notation = []
opr={}
opr['*']= 2
opr['/']= 2
opr['+']= 1
opr['-']= 1

for i in org:
    if i in ascii_uppercase:
        notation.append(i)
    elif i == "(":
        
    elif SS.size()>0:
        if opr[SS.peek()] < opr[i]:
            SS.push(i)
        else:
            while opr[SS.peek()] >= opr[i]:
                notation.append(SS.pop())
                if SS.isEmpty() :
                    break

            SS.push(i)
    else:
        SS.push(i)

while not SS.isEmpty():
    notation.append(SS.pop())

expr=''.join(notation)

print(expr) 