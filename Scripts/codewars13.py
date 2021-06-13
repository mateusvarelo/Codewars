"""Complete the solution so that it returns true if the first argument(string) 
passed in ends with the 2nd argument
(also a string)"""

def solution(string, ending):
    # your code here...
    # cond = (
    #     True if string[len(string):-(len(ending)+1):-1][::-1]==ending 
    #     or len(ending)==0 else False
    # )
    return string.endswith(ending)
print(solution('abcd',''))    
