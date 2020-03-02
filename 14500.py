import sys
N, M = map(int, input().split())
board = [list(map(int, sys.stdin.readline().split())) for i in range(N)]
def horizon(start):
    if 0 <= start[0] <= N-1 and 0 <= start[1] <= M-4:
        return board[start[0]][start[1]] + board[start[0]][start[1]+1] +\
         board[start[0]][start[1] + 2] + board[start[0]][start[1] + 3]
    return 0
def box(start):
    if 0<=start[0]<=N-2 and 0<= start[1] <= M-2:
        return board[start[0]][start[1]] + board[start[0]][start[1]+1] +\
        board[start[0]+1][start[1]] + board[start[0]+1][start[1]+1]
    return 0
def L(start):
    if 0<=start[0]<=N-3 and 0<=start[1]<=M-2:
        return board[start[0]][start[1]] + board[start[0]+1][start[1]]+\
        board[start[0]+2][start[1]] + board[start[0]+2][start[1]+1]
    return 0
def S(start):
    if 0<=start[0]<=N-3 and 0<=start[1]<=M-3:
        return board[start[0]][start[1]] + board[start[0]+1][start[1]]+\
        board[start[0]+1][start[1]+1] + board[start[0]+2][start[1]+1]
    return 0
def Ns(start):
    if 0<=start[0]<=N-2 and 0<=start[1]<=M-3:
        return board[start[0]][start[1]] + board[start[0]][start[1]+1] +\
        board[start[0]][start[1]+2] + board[start[0]+1][start[1]+1]
    return 0
def SS(start):
    if 0<=start[0]<=N-2 and 0<=start[1]<=M-3:
        return board[start[0]][start[1]] + board[start[0]][start[1]+1] +\
        board[start[0]+1][start[1]+1] + board[start[0]+1][start[1]+2]
    return 0

def rotate(board):
    lst = [[0]*N for i in range(M)] #N=4,M=5
    for i in range(N):              # 5,4
        for j in range(M):
            lst[j][N-i-1] = board[i][j]
    return M, N, lst

def turn(board):
    return M, N, list(map(list, zip(*board)))
big = []
for __ in range(2):
    for _ in range(4):
        for x in range(N):
            for y in range(M):
                big.append(horizon([x,y]))
                big.append(box([x,y]))
                big.append(L([x,y]))
                big.append(S([x,y]))
                big.append(Ns([x,y]))
                big.append(SS([x,y]))
        N, M, board = rotate(board)
    N, M, board = turn(board)
print(max(big))