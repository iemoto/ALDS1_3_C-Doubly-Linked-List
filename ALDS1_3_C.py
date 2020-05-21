num = int(input())
stack = []
while num > 0:
  ope , *i  = input().split()
  try:
    i = int(i[0])
  except:
    pass
  if ope == 'insert':
    stack.append(i)
  elif ope == 'delete':
    stack = stack[::-1]
    try:
      stack.remove(i)
    except:
      pass
    stack = stack[::-1]
  elif ope == 'deleteFirst':
    stack.pop(-1)
  elif ope == 'deleteLast':
    stack.pop(0)
  else: print('error')  
  num -= 1
  # print(ope,i)
  # print(stack)
print(*stack[::-1])