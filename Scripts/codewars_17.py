"""
Write a function, persistence,
that takes in a positive parameter num and returns
its multiplicative persistence, which is the number of times you must 
multiply the digits in num until you reach a single digit.
"""


def persistence(n):
     lista = list(str(n))
     lista = list(map(lambda x:int(x),lista))
     if len(lista) == 0
     i = 1
     while i != len(lista):
          lista[i-1]*
          i+= 1
          
                 
     else:
         return 0
     
         
         
print(persistence(44))     