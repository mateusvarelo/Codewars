"""
Clock shows h hours, m minutes and s seconds after midnight.

Your task is to write a function which returns the time since midnight in milliseconds.
"""
def past(h, m, s):
     return (3600*h + 60*m + s) * 1000
print(past(0,0,0))    