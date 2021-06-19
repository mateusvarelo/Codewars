"""
Your task is to make function,
which returns the sum of a sequence of integers.

The sequence is defined by 3 non-negative values:
begin, end, step.

If begin value is greater than the end,
function should returns 0
"""


def sequence_sum(begin_number, end_number, step):
    soma = 0
    if begin_number > end_number:
        return 0
    else:
        for i in range(begin_number,end_number+1,step):
            soma +=i 
    return soma      

print(sequence_sum(16, 15, 3)) 