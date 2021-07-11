def calculate_string(st): 
    n1 = ''
    n2 = ''
    operadores = ['+',' -', '*','/']
    numeros = [str(range(0,10))]
    for letra in st:
      if (letra in numeros) and (letra in operadores):
        n1 =''+letra
print(calculate_string("gdfgdf2.34dg54gf*23oP42"))