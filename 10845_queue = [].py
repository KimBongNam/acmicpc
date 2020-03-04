import sys
queue = []
num = int(input())

for i in range(num):
   order_l = sys.stdin.readline().split()
   if len(order_l) == 2:
      if order_l[0] == 'push':
         queue.append(order_l[1])

   else:
      if order_l[0] == 'pop':
         if len(queue)==0:
            print('-1')
         else:
            print(queue[0])
            del queue[0]
      elif order_l[0] == 'size':
         print(len(queue))

      elif order_l[0] == 'empty':
         if len(queue) == 0:
            print('1')
         else:
            print('0')

      elif order_l[0] == 'front':
         if len(queue) == 0:
            print('-1')
         else:
            print(queue[0])
      elif order_l[0] == 'back':
         if len(queue) == 0:
            print('-1')
         else:
            print(queue[len(queue)-1])
            
            
