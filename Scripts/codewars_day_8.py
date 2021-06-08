"""Given two integers a and b, 
which can be positive or negative,
find the sum of all the integers between and 
including them and return it. 
If the two numbers are equal return a or b.
Note: a and b are not ordered!"""
def get_sum(a,b):
    #good luck!
    return sum(range(min(a, b), max(a, b) + 1))
a,b = 10,5       
print(get_sum(a,b))

