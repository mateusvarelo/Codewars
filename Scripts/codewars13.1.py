def duplicate_encode(word):
    #your code here
    return ''.join(
                  [
                   '(' if word.count(letra)<2 else ')'  
                    for letra in word
             ]
 ) 
print(duplicate_encode("wI(GzSG@)FOdyRQwau(a"))