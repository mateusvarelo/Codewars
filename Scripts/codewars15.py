
def open_or_senior(data):
    dados = [
            'Senior'if (x[0] >= 55) and (x[1] > 7)    
             else 'Open'
             for i,x in enumerate(data)         
    ]
           
    return dados
print(open_or_senior([(45, 12),(55,21),(19, -2),(104, 20)]))