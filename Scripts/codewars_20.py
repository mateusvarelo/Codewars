"""  As a part of this Kata,
you need to create a function that 
when provided with a triplet, 
returns the index of the numerical
element that lies between the other two elements.

The input to 
the function will be an array of 
three distinct numbers (Haskell: a tuple)."""

def gimme(inputArray):
    # Implement this function
    return inputArray.index(sorted(inputArray)[1])      
print(gimme([6,5,14]))        