def duplicate_encode(word):
    #your code here
    return ''.join(
                  [
                   '(' if word.upper().count(letra)<2 else ')'  
                    for letra in word.upper()] 
 )  
    
print(duplicate_encode("wI(GzSG@)FOdyRQwau(a"))