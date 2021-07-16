
class Calculator(object):
  
  def evaluate(self, string):
      listaNum = []
      listaNumeros = [
                      float(i) for i in string
                      if i.isdigit()
      ]
      lista_Op+= '+'
      lista_Operadores = [ operador
                          for operador in string
                          if not operador.isspace()  and not operador.isnumeric()  and operador != '.'
      ]
      
           resultado = []

      for n, op in zip(listaNumeros, listaOp): 
        if op == '/':
          resultado.append(resultado.pop() / n)
        elif op == '':
          resultado.append(resultado.pop() * n)
        elif op == '+':
          resultado.append(n)
        elif op == '-':
          resultado.append(-n)

      return sum(resultado)
num = Calculator()    
print(num.evaluate("2 / 2 + 3 * 4 - 6"))