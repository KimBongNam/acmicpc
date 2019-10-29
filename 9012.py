import sys

class Stack:
    def __init__(self):
        self.lst = []
    def push(self, x):
        self.lst.append(x)
    def pop(self):
        del self.lst[-1]
    def check(self):
        if len(self.lst) == 0:
            print("YES")
        else:
            print("NO")

inp = sys.stdin.readlines()
for i in inp[1:]:
    word = i.split()[0]
    s = Stack()
    p = True
    for j in word:
        if j == '(':
            s.push(j)
        elif j == ')':
            try:
                s.pop()
            except:
                print("NO")
                p = False
                break
    if p:
        s.check()
