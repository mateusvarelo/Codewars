import string
def pig_it(text):
    #your code here
    letra = 'ay'
    lista_palavras = text.split(' ') 
    lista = []
    for pal in lista_palavras:
        primeira_letra = list(pal)[0].lower()
        if primeira_letra in list(string.ascii_lowercase):
            primeira_letra = list(pal)[0]
            lista_letras = list(pal)
            lista_letras.append(primeira_letra)
            lista_letras.append(letra)
            lista_letras.pop(0)
        
            lista.append(''.join(lista_letras))
        else: 
            lista.append(primeira_letra)
                
    return ' '.join(lista)

print(pig_it('Pig latin is cool '))