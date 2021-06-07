import string


def is_pangram(s):
    caracteres =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','!',',']
    lista = list(s.replace(" ","").lower())
    for letra in lista:                             
        if letra not in caracteres:
            return True
    return False
pangram = "The quick, brown fox jumps over the lay dog!"
print(is_pangram(pangram))