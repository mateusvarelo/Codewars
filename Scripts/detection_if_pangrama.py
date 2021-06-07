import string


def is_pangram(s):
    caracteres = list(
                      "abcdefghijklmnopqrstuvwxyz!,"
                     )
   
    for letra in s.replace(" ",""):                              
        if letra.lower()   in caracteres:
            return False
    return True
pangram = "The quick, brown fox jumps over the lazy dog!"
print(is_pangram(pangram))