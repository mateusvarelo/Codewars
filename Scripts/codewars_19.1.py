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
         people[0] = people[0].lower()
         print(people) 
         if i>0:
           people[i] = people[i].upper()
         lista.append(lista)
      return lista
print(wave('Mateus'))