import sys
stack = []
num = int(input())

for i in range(num):
   order =  sys.stdin.readline().strip()
   order_l = order.split(" ")
   if len(order_l) == 2:
      if order_l[0] == 'push':
         stack.append(order_l[1])

   else:
      if order_l[0] == 'pop':
         if len(stack)==0:
            print('-1')
         else:
            print(stack[len(stack)-1])
            del stack[len(stack)-1]
      elif order_l[0] == 'size':
         print(len(stack))

      elif order_l[0] == 'empty':
         if len(stack) == 0:
            print('1')
         else:
            print('0')

      elif order_l[0] == 'top':
         if len(stack) == 0:
            print('-1')
         else:
            print(stack[len(stack)-1])
            
            
