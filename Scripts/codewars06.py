def in_array(array1, array2):
    # your code
    return list(set([
            pal for pal in array1
            for pal2 in array2
            if pal2.find(pal) != -1
    ])
print(in_array(["arp", "mice", "bull"]  ,["lively", "alive", "harp", "sharp", "armstrong"]))