
"""Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces.
"""
def get_count(input_str):
     q = sum(c in 'aeiou' for c in input_str)
    # your code here
     print(q)
     return sum(1 for let in input_str if let in "aeiouAEIOU")
print(get_count("o  kak ushakov lil vo kashu kakao"))