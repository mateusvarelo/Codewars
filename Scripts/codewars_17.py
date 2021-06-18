"""
Write a function, persistence,
that takes in a positive parameter num and returns
its multiplicative persistence, which is the number of times you must 
multiply the digits in num until you reach a single digit.
"""


def persistence(n):
     if len(n) == 1:
          return 0
     else:
          soma = list(map(lambda x,y:x*y,list(str(n)) ))
         
         
print(persistence(44))     