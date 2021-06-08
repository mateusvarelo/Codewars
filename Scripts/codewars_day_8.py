"""Given two integers a and b, 
which can be positive or negative,
find the sum of all the integers between and 
including them and return it. 
If the two numbers are equal return a or b.
Note: a and b are not ordered!"""
def get_sum(a,b):
    #good luck!
    lista = [a,b]
    lista.sort()
    if (a==b):
        return a
    else:    
        soma_lista = [i for i in range(lista[0],lista[1]+1)]
    return sum(soma_lista)
        

    
        
