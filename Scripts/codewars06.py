def in_array(array1, array2):
    # your code
     r = list(set([
            pal for pal in array1
            for pal2 in array2
            if pal2.find(pal) != -1
    ]))
     r.sort()
     return r
a1 = ['arp', 'strong', 'live'] 
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
print(in_array(a1,a2))