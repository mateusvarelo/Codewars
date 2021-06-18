"""
An isogram is a word that has no repeating letters,
consecutive or non-consecutive. 
Implement a function that determines whether a string that contains
only letters is an isogram.
Assume the empty string is an isogram. 
Ignore letter case.
"""
def is_isogram(string):
    #your code here
    return len(string) == len(set(string.lower()))
    # pilha = []
    # if len(string) == 0:
    #     return True
    # else:
    #     for letra in string:
    #         letra = letra.lower()
    #         if letra in pilha:
    #             return False
    #         pilha.append(letra)
    # return True 
print(is_isogram('abc'))    