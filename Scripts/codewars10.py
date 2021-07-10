import re
def solution(s):  
   return ' '.join(re.findall('[a-zA-Z][^A-Z]*', s))
print(solution('camelCasing'))