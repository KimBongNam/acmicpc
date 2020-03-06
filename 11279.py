import sys
N = int(input())
13

lst = [int(sys.stdin.readline()) for _ in range(N)]
0
1
2
0
0
3
2
1
0
0
0
0
0

ans = []
for i in lst:
    if i == 0:
        print(0 if len(ans)==0 else "????")
    else:
