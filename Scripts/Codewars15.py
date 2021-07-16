import re
class Calculator(object):
  
  def evaluate(self, string):
      listaNum = []
      listaNum = re.findall(r'\d.?\d*', string)
      lista_Numeros = [float(i) for i in listaNum]
  
      lista_Operadores = [ operador
                          for operador in string
                          if not operador.isspace()  and not operador.isnumeric() and operador != '.'
      ]
      
      lista_Operadores.insert(0,'+')
      resultado = []
      zipado = list(zip(lista_Numeros, lista_Operadores))
      
      for num, op in zipado: 
          if op == '/':
            resultado.append(resultado.pop() / num)
          elif op == '*':
            resultado.append(resultado.pop() * num)
          elif op == '+':
            resultado.append(num)
          elif op == '-':
            resultado.append(-num)
      return sum(resultado)
num = Calculator()    
print(num.evaluate("1.1 + 2.2 + 3.3"))