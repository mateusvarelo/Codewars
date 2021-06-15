
def open_or_senior(data):
    
    dados = list(map(lambda x:list(x),data))
    data.clear()
    # data = [ 
    #               "Senior" if idade[0] > 55 and 
    #               handicap[1] > 7 else "Open"
                  
    # ]
    for i,idade in enumerate(dados):
         for j in range(len(idade)):
             print(idade[j])
    return data

print(open_or_senior([(45, 12),(55,21),(19, -2),(104, 20)]))