"""
In this little assignment you are given a 
string of space separated numbers, 
and have to return the highest and lowest number.
"""
def high_and_low(numbers):
    # ...
    x = list(numbers)
    print(x)
    lista = [max(list(numbers)),]
    print(lista)
    return "".join(lista)
print(high_and_low("1 2 3 4 5"))