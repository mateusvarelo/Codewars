def twos_difference(lst): 
    # your code here
    tm = len(lst)
    lista = []
    for i in range(tm):
        for j in range(tm):
           try:
              dif = lst[i]-lst[j+1]
              if dif == -2 or dif == 2:
                  lista.append((lst[i],lst[j+1]))
           except:
              print('')  
    lista  = list((map(tuple,list(map(sorted,lista)))))         
    return sorted(set(lista))  
                   
print(twos_difference([1, 2, 3, 4])) 