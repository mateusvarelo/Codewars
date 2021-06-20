"""
The wave (known as the Mexican wave in the English-speaking world outside
North America) is an example of metachronal rhythm achieved
in a packed stadium when successive groups of spectators briefly 
stand, yell, and raise their arms. Immediately upon stretching to full height,
the spectator returns to the usual seated position.
"""
#kata Mexican Wave
def wave(people):
      lista = []
      novalista = list(people)
      for i in range(len(people)):
         
         print(people) 
         if i>0:
             novalista.append(people[i].upper())
         else:
             novalista.insert(0,people[0].lower())  
         lista.append(''.join(novalista))
      return lista
print(wave('Mateus'))