def in_array(array1, array2):
    # your code
    return sorted({sub for sub in array1 if any(sub in s for s in array2)})
a1 = ['arp', 'strong', 'live'] 
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
print(in_array(a1,a2))