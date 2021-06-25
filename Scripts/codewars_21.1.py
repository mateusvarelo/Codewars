"""
In this little assignment you are given a 
string of space separated numbers, 
and have to return the highest and lowest number.
"""
def high_and_low(numbers):
    numbers = numbers.replace(" ","")
    return f"{max(list(numbers))} {min(list(numbers))}"
print(high_and_low("1 0 -1"))