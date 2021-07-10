import re
def solution(s):  
   return re.findall('[a-zA-Z][^A-Z]*', s)
print(solution('camelCasing'))