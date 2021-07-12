def twos_difference(lst): 
    # your code here
    tm = len(lst)
    lista = []
    for i in range(tm):
        for j in range(tm):
           try:
              dif = lst[i]-lst[j+1]
              if dif == -2 or dif == 2:
                  lista = set(sorted(lista.append(sorted(lst[i],lst[j+1]))))
           except:
              print('')  
    return lista   
                   
print(twos_difference([1, 2, 3, 4])) 