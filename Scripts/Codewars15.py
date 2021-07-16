import re
class Calculator(object):
  
  def evaluate(self, string):
      listaNumeros = []
      listaNum = []
      listaOp = []

      listaNum = re.findall(r'\d.?\d', string)
      for i in listaNum:
        listaNumeros.append(float(i))

      listaOp.append('+')
      for op in string:
        if op.isspace() == False and op.isnumeric() == False and op != '.': 
          listaOp.append(op)
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