class Calculator(object):
  def evaluate(self, string):
           return f'{string[0::]}'
c = Calculator()
print(c.evaluate("2 / 2 + 3 * 4 - 6"))