import sys
T = int(input())
for _ in range(T):
    Q = int(input())
    lst = []
    for __ in range(Q):
        command = sys.stdin.readline().split()
        if command[0] == 'I':
            lst.append(int(command[1]))
        else:
            if len(lst) != 0:
                if command[1] == '1':
                    idx = 0
                    for i in range(len(lst)):
                        if lst[i] > lst[idx]:
                            idx = i
                    del lst[idx]
                else:
                    idx = 0
                    for i in range(len(lst)):
                        if lst[i] < lst[idx]:
                            idx = i
                    del lst[idx]
    if len(lst)==0:
        print("EMPTY")
    else:
        print(max(lst), min(lst))