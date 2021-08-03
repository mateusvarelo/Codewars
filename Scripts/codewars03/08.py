
def pig_it(text):
    #your code here
    lst = text.split()
    return (
         ' '.join(
             [word[1:] + word[:1]
             + 'ay' if word.isalpha() else word 
             for word in lst]
             )
)

print(pig_it('Pig latin is cool ! '))