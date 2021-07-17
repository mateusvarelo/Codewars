"""
Write a function, persistence,
that takes in a positive parameter num and returns
its multiplicative persistence, which is the number of times you must 
multiply the digits in num until you reach a single digit.
"""
def persistence(n):
    # your
    cont = 0
    n = list(str(n))
    
    if len(n) != 1:
      while len(n)!=1:
           n = numpy.prod(list(map(int,n))) 
           n = list(str(n)) 
           cont +=1
      else:
           return cont
    else:
      return 0     
print(persistence(44))     