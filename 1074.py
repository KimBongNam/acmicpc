import sys
sys.setrecursionlimit(100000)
N, r, c = map(int, input().split())

def resize(N, row, col):
    if row==0 and col == 0:
        return 0
    elif row == 0 and col == 1:
        return 1
    elif row == 1 and col == 0:
        return 2
    elif row == 1 and col == 1:
        return 3
    elif row < (2 ** N)//2 and col < (2**N)//2:
        return resize(N-1, row, col)
    elif row < (2**N) //2 and col >= (2**N)//2:
        return ((2**N)*(2**N))//4 + resize(N-1, row, col-(2**N)//2)
    elif row >= (2**N)//2 and col < (2**N)//2:
        return (((2**N)*(2**N))//4)*2 + resize(N-1, row-(2**N)//2, col)
    elif row >= (2**N)//2 and col >= (2**N)//2:
        return (((2**N)*(2**N))//4)*3 + resize(N-1, row-(2**N)//2, col-(2**N)//2)

print(resize(N,r,c))