import sys
deque = []
num = int(input())
15
for i in range(num):
    order = sys.stdin.readline().split()   
    if order[0] == "push_front":
        deque = [order[1]] + deque
    elif order[0] == "push_back":
        deque.append(order[1])
    elif order[0] == "pop_front":
        print(deque.pop(0) if len(deque)!=0 else -1)
    elif order[0] == "pop_back":
        print(deque.pop() if len(deque)!=0 else -1)
    elif order[0] == "size":
        print(len(deque))
    elif order[0] == "empty":
        print(1 if len(deque)==0 else 0)
    elif order[0] == "front":
        print(-1 if len(deque)==0 else deque[0])
    elif order[0] == "back":
        print(-1 if len(deque)==0 else deque[-1])
