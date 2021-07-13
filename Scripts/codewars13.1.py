def duplicate_encode(word):
    #your code here
    tm =len(word.split())-1
    lista = word.split()
    print(lista[tm])
    return ''.join(
                  [
                   '(' if word.count(letra)<2 else ')'  
                    for letra in lista[tm]] 
 )  
print(duplicate_encode("aaa aaavb wI(GzSG@)FOdyRQwau(a"))