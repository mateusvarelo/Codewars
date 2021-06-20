"""  As a part of this Kata,
you need to create a function that 
when provided with a triplet, 
returns the index of the numerical
element that lies between the other two elements.

The input to 
the function will be an array of 
three distinct numbers (Haskell: a tuple)."""

def gimme(input_array):
    # Implement this function
    for i,valor in enumerate(input_array):
        if (min(input_array) == valor):
             continue 
        elif (max(input_array)== valor):  
             continue
        else:
             return i       
print(gimme([5,10,14]))        