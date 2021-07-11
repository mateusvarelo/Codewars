def calculate_string(st): 
    clear_string = ''
    operadores = ['+','-', '*','/']
    numeros = [str(i) for i in range(10)]
    for letra in st:
      if (letra in numeros) or (letra in operadores) or (letra == '.'):
         clear_string = f'{clear_string}{letra}'
    for let in clear_string:
          if let in operadores:
              lista = clear_string.split(let)  
              if let == '*':   
                 return  str(int(float(lista[0])*float(lista[1])))
              elif let == '+':
                 return  str(int(float(lista[0])+float(lista[1])))
              elif let == '/':
                 return  str(int(float(lista[0])/float(lista[1])))
              elif let == '-':
                 return  str(round((float(lista[0])-float(lista[1]))))        
print(calculate_string("fsdfsd235???34.4554s4234df-sdfgf2g3h4j442"))