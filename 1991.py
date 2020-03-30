import sys
from string import ascii_uppercase
N = int(input())
tree = {i:[] for i in ascii_uppercase[:N]}
for _ in range(N):
    root, left, right = sys.stdin.readline().split()
    tree[root].extend([left, right])

def preorder(pos, queue):
    queue.append(pos)
    if tree[pos][0] != '.':
        preorder(tree[pos][0], queue)
    if tree[pos][1] != '.':
        preorder(tree[pos][1], queue)

def inorder(pos, queue):
    if tree[pos][0] != '.':
        inorder(tree[pos][0], queue)
    queue.append(pos)
    if tree[pos][1] != '.':
        inorder(tree[pos][1], queue)

def postorder(pos, queue):
    if tree[pos][0] != '.':
        postorder(tree[pos][0], queue)
    if tree[pos][1] != '.':
        postorder(tree[pos][1], queue)
    queue.append(pos)

queue = []
preorder('A', queue)
print(*queue, sep='')

queue = []
inorder('A', queue)
print(*queue, sep='')

queue = []
postorder('A', queue)
print(*queue, sep='')