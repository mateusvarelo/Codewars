def in_array(array1, array2):
    # your code
    r = [
            pal for pal in array1
            for pal2 in array2
            if pal2.find(pal) != -1
    ]
    return list(set(r))
print(in_array(["arp", "mice", "bull"]  ,["lively", "alive", "harp", "sharp", "armstrong"]))