def fib_recursion(num):
  if num==1 or num==0:
    return num
  else:
    return fib_recursion(num-1) + fib_recursion(num-2)

print(fib_recursion(10))