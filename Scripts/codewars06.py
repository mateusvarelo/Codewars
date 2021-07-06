def in_array(array1, array2):
    # your code
    r = []
    for pal in array1:
        for pal2 in array2:
           if pal2.find(pal) == -1:
               continue
           else:    
               r.append(pal)   
    r.sort()
    return set(r)
print(in_array(["live", "arp", "strong"] ,["lively", "alive", "harp", "sharp", "armstrong"]))