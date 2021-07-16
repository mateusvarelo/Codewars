
class Calculator(object):
  
  def evaluate(self, string):
      listaNum = []
      lista_Numeros = [
                      float(i) for i in string
                      if i.isdigit()
      ]
      lista_Operadores = [ operador
                          for operador in string
                          if not operador.isspace()  and not operador.isnumeric()  and operador != '.'
      ]
      #lista_Operadores.insert(0,'+')
      print(lista_Operadores)
      resultado = []

      for num, op in zip(lista_Numeros, lista_Operadores): 
        try:
          if op == '/':
            resultado.append(resultado.pop() / num)
          elif op == '':
            resultado.append(resultado.pop() * num)
          elif op == '+':
            resultado.append(num)
          elif op == '-':
            resultado.append(-num)
        except:
             continue
      return sum(resultado)
num = Calculator()    
print(num.evaluate("2 / 2 + 3 * 4 - 6"))