N = int(input())
move = []
def hanoi(n,start, mid, end, move):
    if n == 1:
        move.append([start,end])
    else:
        hanoi(n-1,start,end,mid, move)
        move.append([start,end])
        hanoi(n-1,mid,start,end, move)

hanoi(N,1,2,3, move)

print(len(move))
for i in move:
    print(i[0], i[1])