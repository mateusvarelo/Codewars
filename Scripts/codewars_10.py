def summation(num):
    soma = 1 if num <= 1 else  sum(range(1,num+1))
    return soma
print(summation(22))    