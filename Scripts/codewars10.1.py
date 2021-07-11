def calculate_string(st): 
    clear_string = ''
    operadores = ['+',' -', '*','/']
    numeros = [str(i) for i in range(10)]
    for letra in st:
      if (letra in numeros) or (letra in operadores) or (letra == '.'):
         clear_string = f'{clear_string}{letra}'
    for let in clear_string:
          if let in operadores:
              lista = clear_string.split(let)  
              return f'{float(lista[0])}{let}{float(lista[1])}'      
print(calculate_string("gdfgdf2.34dg54gf*23oP42"))