###################################
# Logic: recursive/ loop
###################################
def fib_0(n):
  '''
  normal 
  '''
  fib_pair = [0, 1]
  for i in xrange(n):
    fib_pair = [fib_pair[1], fib_pair[0]+fib_pair[1]]
  return fib_pair[0]


def fib_1(n):
  '''
  reduce https://docs.python.org/2/library/functions.html#reduce
  '''
  fib_pair = reduce(lambda x, n: [x[1], x[0]+x[1]],
                xrange(n), 
                [0, 1])
  return fib_pair[0]

# lambda 
fib_2 = lambda n : reduce(lambda x, n: [x[1], x[0]+x[1]], xrange(n), [0, 1])[0]




###################################
# Logic: closed-form
###################################
def fib_3(n): 
  '''
  X2=X1+x0
  Characteristic equation x^2 = X + 1
  x_{n} = \cfrac{1}{\sqrt{5}}\cdot\left(\cfrac{1+\sqrt{5}}{2}\right)^n-\cfrac{1}{\sqrt{5}}\cdot\left(\cfrac{1-\sqrt{5}}{2}\right)^n~.
  
  * suffering from cost of float number calculation 
  * cannot use ** since it calculates nearest int value 
  * not accurate since floating number 
  '''
  
  import math
  f_n = 1/math.sqrt(5) * math.pow((1+math.sqrt(5))/2, n) - 1/math.sqrt(5) * math.pow((1-math.sqrt(5))/2, n)
  return int(f_n+0.5)
  

def fib_4(n):
  '''
  Matrix Form 

  {F_{k+2} \choose F_{k+1}} &= \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix} {F_{k+1} \choose F_{k}} 

  http://en.wikipedia.org/wiki/Fibonacci_number#Matrix_form
  '''
  if n==0:
    return 0
  a = [
  [1, 1],
  [1, 0]
  ]

  for i in xrange(n-1):
    # matrix multiplication 
    a = [
    [a[0][0]+a[1][0], a[1][0]+a[1][1]],
    [a[0][0], a[0][1]]
    ]  
    
  return a[0][1]




if __name__=="__main__":
  assert fib_0(100)==354224848179261915075
  assert fib_1(100)==fib_0(100)
  assert fib_2(100)==fib_0(100)
  assert fib_3(50)==fib_0(50)
  assert fib_4(100)==fib_0(100)


  

